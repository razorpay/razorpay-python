## POS Gateway Integration

Complete guide for integrating Razorpay POS Gateway with Device Activity and Order management APIs.

## Quick Start

```py
import razorpay

# Initialize client
client = razorpay.Client(auth=('your_key_id', 'your_key_secret')) # Defautl base_url: 'https://api.razorpay.com'

# For local development/testing
client = razorpay.Client(
    auth=('your_key_id', 'your_key_secret'),
    base_url='http://localhost:PORT'
)
```

**Host Configuration:**
- **Production**: `https://api.razorpay.com` (default)
- **Pos-Gateway**: `http://localhost:PORT`

---

## Core APIs

### 1. Order Management

#### Create Order

```py
order = client.order.create({
    "amount": 19900,                        # Required: Amount in paise (₹199.00)
    "currency": "INR",                      # Required: Currency
    "receipt": "order_rcptid_11",           # Optional: Receipt ID
    "notes": {                              # Optional: Additional notes
        "key1": "value1",
        "key2": "value2"
    }
}, device_mode="wired")  # Required: "wired" or "wireless"
```

**Parameters:**

| Name          | Type    | Description                                                                    |
|---------------|---------|--------------------------------------------------------------------------------|
| amount*       | integer | Amount in paise (₹199.00 = 19900)                                            |
| currency*     | string  | Currency code (e.g., "INR")                                                   |
| receipt       | string  | Your system order reference ID                                                 |
| notes         | object  | A key-value pair for additional information                                    |
| device_mode*  | string  | Device communication mode. Possible values: `wired`, `wireless`               |

**Success Response:**

```json
{
  "id": "order_R7vqkfqG3Iw02m",
  "entity": "order",
  "amount": 19900,
  "amount_paid": 0,
  "amount_due": 19900,
  "currency": "INR",
  "receipt": "order_rcptid_11",
  "status": "created",
  "attempts": 0,
  "notes": {
    "key1": "value1",
    "key2": "value2"
  },
  "created_at": 1641891747
}
```

**Failure Response:**

```json
{
  "error": {
    "code": "BAD_REQUEST_ERROR",
    "description": "The amount must be at least INR 1.00",
    "source": "business",
    "step": "payment_initiation",
    "reason": "input_validation_failed"
  }
}
```

---

#### Get Order Details

```py
order = client.order.fetch(
    "order_R7vqkfqG3Iw02m",
    device_mode="wired"  # Required: "wired" or "wireless"
)
```

**Parameters:**

| Name          | Type   | Description                                                                    |
|---------------|--------|--------------------------------------------------------------------------------|
| order_id*     | string | Order ID to fetch details for                                                 |
| device_mode*  | string | Device communication mode. Possible values: `wired`, `wireless`               |

**Success Response:**

```json
{
  "id": "order_R7vqkfqG3Iw02m",
  "entity": "order",
  "amount": 19900,
  "amount_paid": 19900,
  "amount_due": 0,
  "currency": "INR",
  "receipt": "order_rcptid_11",
  "status": "paid",
  "attempts": 1,
  "notes": {
    "key1": "value1",
    "key2": "value2"
  },
  "created_at": 1641891747
}
```

**Failure Response:**

```json
{
  "error": {
    "code": "BAD_REQUEST_ERROR",
    "description": "The id provided does not exist",
    "source": "business",
    "step": "payment_initiation",
    "reason": "input_validation_failed"
  }
}
```

---

#### Get Order with Payments

```py
order_with_payments = client.order.fetch(
    "order_R7vqkfqG3Iw02m",
    data={"expand[]": "payments"},
    device_mode="wired"  # Required: "wired" or "wireless"
)
```

**Parameters:**

| Name          | Type   | Description                                                                    |
|---------------|--------|--------------------------------------------------------------------------------|
| order_id*     | string | Order ID to fetch details for                                                 |
| data*         | object | Expansion parameters: `{"expand[]": "payments"}`                              |
| device_mode*  | string | Device communication mode. Possible values: `wired`, `wireless`               |

**Success Response:**

```json
{
  "id": "order_R7vqkfqG3Iw02m",
  "entity": "order",
  "amount": 19900,
  "amount_paid": 19900,
  "amount_due": 0,
  "currency": "INR",
  "receipt": "order_rcptid_11",
  "status": "paid",
  "attempts": 1,
  "notes": {
    "key1": "value1",
    "key2": "value2"
  },
  "created_at": 1641891747,
  "payments": {
    "entity": "collection",
    "count": 1,
    "items": [
      {
        "id": "pay_G8VQzjPLoAvm6D",
        "entity": "payment",
        "amount": 19900,
        "currency": "INR",
        "status": "captured",
        "order_id": "order_R7vqkfqG3Iw02m",
        "method": "upi",
        "description": "POS Transaction",
        "created_at": 1641891755,
        "upi": {
          "payer_account_type": "bank_account",
          "vpa": "gaurav.kumar@example"
        }
      }
    ]
  }
}
```

**Failure Response:**

```json
{
  "error": {
    "code": "BAD_REQUEST_ERROR",
    "description": "The id provided does not exist",
    "source": "business",
    "step": "payment_initiation",
    "reason": "input_validation_failed"
  }
}
```

### 2. Device Activity Management

For detailed API reference, see [Device Activity](deviceActivity.md).

#### Initiate Checkout

```py
response = client.device_activity.create({
    "device_id": "2841158834",            # Required for device_mode="wireless", optional for device_mode="wired"
    "action": "initiate_checkout",        # Required: Action type
    "notes": {                            # Optional: Additional notes
        "key1": "value1",
        "key2": "value2"
    },
    "initiate_checkout": {               # Required for initiate_checkout
        "name": "Acme Corp",             # Optional: Business name
        "amount": 19900,                 # Required: Amount in paise (₹199.00)
        "currency": "INR",               # Required: Currency code
        "description": "POS Transaction", # Required: Transaction description
        "type": "in_person",             # Optional: Transaction type
        "order_id": "order_R7vqkfqG3Iw02m", # Required: Order reference
        "prefill": {                     # Optional: Customer prefill data
            "name": "Gaurav Kumar",
            "email": "gaurav.kumar@example.com",
            "contact": "9000090000",
            "method": "upi"              # Optional: "upi"|"card"
        }
    }
}, device_mode="wired")  # Required: "wired" or "wireless"
```

#### Close Checkout

```py
response = client.device_activity.create({
    "device_id": "2841158834",           # Required for device_mode="wireless", optional for device_mode="wired"
    "action": "close_checkout"           # Required: Action type
}, device_mode="wireless")  # Required: "wired" or "wireless"
```


---

## Device Modes

| Mode | Description | device_id Required |
|------|-------------|-------------------|
| **wireless** | Wireless communication | ✅ Yes |
| **wired** | Direct device connection | ❌ Optional |

---

## Complete Integration Workflow

```py
import razorpay
import time

class POSIntegration:
    def __init__(self, key_id, key_secret, base_url=None):
        """Initialize POS integration client"""
        self.client = razorpay.Client(
            auth=(key_id, key_secret),
            base_url=base_url
        )

    def complete_pos_checkout(self, device_id, amount, device_mode="wired"):
        """Complete end-to-end POS checkout process"""
        try:
            # Step 1: Create Order
            order = self.client.order.create({
                "amount": amount,
                "currency": "INR",
                "receipt": f"pos_order_{int(time.time())}",
                "notes": {"device_id": device_id}
            }, device_mode=device_mode)
            
            print(f"Order created: {order['id']}")
            
            # Step 2: Initiate Device Checkout
            activity = self.client.device_activity.create({
                "device_id": device_id,
                "action": "initiate_checkout",
                "notes": {"order_id": order['id']},
                "initiate_checkout": {
                    "name": "Acme Corp",
                    "amount": amount,
                    "currency": "INR",
                    "description": "POS Transaction",
                    "type": "in_person",             # Optional
                    "order_id": order['id'],
                    "prefill": {
                        "name": "Customer Name",
                        "email": "customer@example.com",
                        "contact": "9000090000",
                        "method": "upi"
                    }
                }
            }, device_mode=device_mode)
            
            activity_id = activity['id']
            print(f"Checkout initiated: {activity_id}")
            
            print("Checkout initiated successfully")

            self.close_checkout(device_mode=device_mode)
            
            return {
                "success": True,
                "order": order,
                "activity": activity
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def close_checkout(self, device_mode):
        """Close active checkout"""
        try:
            return self.client.device_activity.create({
                "device_id": "2841158834",  # Use your device ID
                "action": "close_checkout"
            }, device_mode=device_mode)
        except Exception as e:
            print(f"Failed to close checkout: {e}")
            return None

# Usage Example
pos = POSIntegration('your_key_id', 'your_key_secret')
result = pos.complete_pos_checkout(
    device_id="2841158834",
    amount=19900,  # ₹199.00
    device_mode="wired"
)

if result['success']:
    print("✅ Checkout completed successfully!")
    print(f"Order ID: {result['order']['id']}")
else:
    print(f"❌ Checkout failed: {result['error']}")
```

---

## Error Handling

```py
from razorpay.errors import BadRequestError

try:
    response = client.device_activity.create(data, device_mode="wired")
except BadRequestError as e:
    if "Invalid device mode" in str(e):
        print("Use 'wired' or 'wireless' for device_mode")
    elif "Invalid activity data" in str(e):
        print("Provide valid activity data")
    else:
        print(f"API Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

**Common Error Solutions:**

| Error | Cause | Solution |
|-------|-------|----------|
| `Invalid device mode` | Wrong device_mode value | Use `"wired"` or `"wireless"` |
| `device_id required for wireless mode` | Missing device_id | Include device_id for wireless mode |

**API Response Status Handling:**

```py
# Check status in response
if response['status'] == 'processing':
    print("Checkout initiated, waiting for completion...")
elif response['status'] == 'completed':
    print("Checkout completed successfully!")
elif response['status'] == 'failed':
    error_code = response['error']['code']
    error_reason = response['error']['reason']
    print(f"Checkout failed: {error_code} - {error_reason}")
```

**Device Activity API Error Codes:**

| Error Code | Reason | Description | Solution |
|------------|--------|-------------|----------|
| `BAD_REQUEST_ERROR` | `device_not_connected` | Device is not connected | Check device connection and retry |
| `BAD_REQUEST_ERROR` | `checkout_not_found` | Checkout session not found | Verify checkout was initiated |

**Order API Error Codes:**

| Error Code | Reason | Description | Solution |
|------------|--------|-------------|----------|
| `BAD_REQUEST_ERROR` | `input_validation_failed` | Invalid parameters provided | Check amount, currency, and other parameters |
| `BAD_REQUEST_ERROR` | Order not found | The order ID does not exist | Verify the correct order ID |

---

## Complete API Reference Summary

### Device Activity APIs

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `create()` | `data`, `device_mode` | Activity object with status | Create checkout activity |

**Usage Examples:**
```py
# Initiate checkout
activity = client.device_activity.create(data, device_mode="wired")

# Close checkout
client.device_activity.create({"action": "close_checkout"}, device_mode="wired")
```

### Order APIs

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `create()` | `data`, `device_mode` | Order object | Create new order |
| `fetch()` | `order_id`, `device_mode` | Order object | Get order details |
| `fetch()` with payments | `order_id`, `data`, `device_mode` | Order with payments | Get order with payment details |

**Usage Examples:**
```py
# Create order
order = client.order.create(order_data, device_mode="wired")

# Fetch order
order = client.order.fetch("order_123", device_mode="wired")  

# Fetch order with payments
order_with_payments = client.order.fetch("order_123", data={"expand[]": "payments"}, device_mode="wired")
```

---

## API Error Codes and Messages

This section provides comprehensive error information that clients may encounter when calling POS Gateway APIs.

### Error Response Format

All APIs return errors in the following standardized format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "description": "Human-readable error message",
    "source": "error_source",
    "step": "operation_step",
    "reason": "technical_reason",
    "field": "field_name",
    "metadata": {
      "additional": "context"
    }
  }
}
```

**Error Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| code | string | Error code identifier |
| description | string | Human-readable error message |
| source | string | Component that generated the error |
| step | string | Operation step where error occurred (optional) |
| reason | string | Technical reason for the error (optional) |
| field | string | Field that caused validation error (optional) |
| metadata | object | Additional error context (optional) |

---

### Device Activity API Errors

#### POST /v1/devices/activity

**HTTP Status Codes:**
- `200` - Success
- `400` - Validation errors
- `500` - Processing/Device errors

**Common Error Scenarios:**

```json
// Missing required field
{
  "error": {
    "code": "VALIDATION_FAILED",
    "description": "Action field is required",
    "source": "activity_processor",
    "field": "action",
    "reason": "required_field_missing"
  }
}

// Invalid amount
{
  "error": {
    "code": "VALIDATION_FAILED", 
    "description": "Amount must be greater than 0",
    "source": "activity_processor",
    "field": "initiate_checkout.amount",
    "reason": "invalid_value"
  }
}

// Device not connected
{
  "error": {
    "code": "DEVICE_DISCONNECTED",
    "description": "Device is not connected",
    "source": "device_controller"
  }
}

// Device busy/invalid state
{
  "error": {
    "code": "DEVICE_BUSY",
    "description": "Device is in an invalid state or transitioning",
    "source": "device_controller"
  }
}
```

**Validation Error Codes:**

| Error Code | Field | Description | Solution |
|------------|-------|-------------|----------|
| `VALIDATION_FAILED` | `action` | Missing action field | Provide `"initiate_checkout"` or `"close_checkout"` |
| `VALIDATION_FAILED` | `initiate_checkout.amount` | Invalid or missing amount | Provide amount > 0 in paise |
| `VALIDATION_FAILED` | `initiate_checkout.currency` | Missing currency | Provide currency code (e.g., "INR") |
| `VALIDATION_FAILED` | `initiate_checkout.order_id` | Missing order ID | Provide valid order ID |
| `VALIDATION_FAILED` | `device_id` | Missing device ID | Required for wireless mode |
| `VALIDATION_FAILED` | `device_mode` | Invalid communication mode | Use `"wired"` or `"wireless"` |

**Device Error Codes:**

| Error Code | Description | Solution |
|------------|-------------|----------|
| `DEVICE_DISCONNECTED` | Device is not connected | Check device connection and retry |
| `DEVICE_NOT_FOUND` | Device not found during discovery | Verify device is connected and powered on |
| `DEVICE_BUSY` | Device is in invalid state | Wait for current operation to complete |
| `DEVICE_TIMEOUT` | Device operation timed out | Check device connection and retry |
| `DEVICE_ERROR` | Generic device communication error | Check device status and connection |
| `UNSUPPORTED_ACTION` | Invalid action for device state | Verify device supports the requested action |

#### GET /v1/devices/activity/{activity_id}

**HTTP Status Codes:**
- `200` - Success
- `400` - Invalid activity ID
- `404` - Activity not found
- `500` - Processing errors

**Error Examples:**

```json
// Activity not found
{
  "error": {
    "code": "ACTIVITY_NOT_FOUND",
    "description": "Activity with given ID not found",
    "source": "activity_processor"
  }
}

// Invalid activity ID format
{
  "error": {
    "code": "VALIDATION_FAILED",
    "description": "Invalid activity ID format",
    "source": "activity_processor",
    "field": "activity_id"
  }
}
```

---

### Order API Errors

#### POST /v1/orders

**HTTP Status Codes:**
- `200` - Success
- `400` - Validation errors
- `500` - Processing errors

**Common Error Scenarios:**

```json
// Missing required field
{
  "error": {
    "code": "VALIDATION_FAILED",
    "description": "Amount field is required",
    "source": "order_processor",
    "field": "amount",
    "reason": "required_field_missing"
  }
}

// Invalid amount
{
  "error": {
    "code": "VALIDATION_FAILED",
    "description": "Amount must be at least INR 1.00",
    "source": "order_processor",
    "field": "amount",
    "reason": "amount_too_small"
  }
}

// Device in proxy mode
{
  "error": {
    "code": "BUSINESS_LOGIC_ERROR",
    "description": "Device is in proxy mode, cannot process order",
    "source": "order_processor"
  }
}
```

**Order Validation Errors:**

| Error Code | Field | Description | Solution |
|------------|-------|-------------|----------|
| `VALIDATION_FAILED` | `amount` | Missing or invalid amount | Provide amount ≥ 100 paise (₹1.00) |
| `VALIDATION_FAILED` | `currency` | Missing or invalid currency | Provide valid currency code (e.g., "INR") |
| `VALIDATION_FAILED` | `device_mode` | Missing communication mode | Use `"wired"` or `"wireless"` |

#### GET /v1/orders/{order_id}

**HTTP Status Codes:**
- `200` - Success
- `400` - Invalid order ID
- `404` - Order not found
- `500` - Processing errors

**Error Examples:**

```json
// Order not found
{
  "error": {
    "code": "ORDER_NOT_FOUND",
    "description": "Order with given ID not found",
    "source": "order_processor"
  }
}
```

---

### Device-Specific Error Codes

These errors originate from the physical POS device:

**Card Transaction Errors:**

```json
{
  "error": {
    "code": "CARD_DECLINED",
    "description": "Transaction was declined by the card issuer",
    "source": "DEVICE",
    "step": "AUTHORIZATION",
    "reason": "Insufficient funds"
  }
}
```

**Common Device Error Codes:**

| Error Code | Description | User Action |
|------------|-------------|-------------|
| `CARD_DECLINED` | Card transaction declined | Try different card or payment method |
| `CARD_READ_ERROR` | Failed to read card data | Clean card and retry insertion |
| `INVALID_PIN` | Incorrect PIN entered | Re-enter correct PIN |
| `TIMEOUT` | Transaction timed out | Retry transaction |
| `TRANSACTION_CANCELLED` | User cancelled transaction | Restart checkout if needed |
| `NETWORK_ERROR` | Device network connectivity issue | Check device network connection |
| `DEVICE_MALFUNCTION` | Hardware malfunction | Contact support |

---

### HTTP Status Code Reference

| Status Code | Meaning | When It Occurs |
|-------------|---------|----------------|
| `200` | Success | Request processed successfully |
| `400` | Bad Request | Validation errors, malformed requests |
| `401` | Unauthorized | Authentication failed (proxy mode) |
| `404` | Not Found | Resource not found (order/activity ID) |
| `500` | Internal Server Error | Device errors, system failures |

---

### Error Handling Best Practices

**1. Retry Logic:**
```python
import time

def retry_device_operation(operation_func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return operation_func()
        except Exception as e:
            error_code = getattr(e, 'code', None)
            
            # Retry for transient errors
            if error_code in ['DEVICE_BUSY', 'DEVICE_TIMEOUT', 'DEVICE_DISCONNECTED']:
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                    continue
            raise e
```

**2. Error Classification:**
```python
def classify_error(error_response):
    error_code = error_response.get('error', {}).get('code', '')
    
    # Validation errors - fix request
    if error_code == 'VALIDATION_FAILED':
        return 'CLIENT_ERROR'
    
    # Device errors - may be transient
    if error_code.startswith('DEVICE_'):
        return 'DEVICE_ERROR'
    
    # System errors - retry or escalate
    if error_code in ['PROCESSING_FAILED', 'BUSINESS_LOGIC_ERROR']:
        return 'SYSTEM_ERROR'
    
    return 'UNKNOWN_ERROR'
```

**3. User-Friendly Messages:**
```python
ERROR_MESSAGES = {
    'DEVICE_DISCONNECTED': 'Please check if the POS device is connected and try again.',
    'CARD_DECLINED': 'Your card was declined. Please try a different payment method.',
    'DEVICE_TIMEOUT': 'The device is taking too long to respond. Please try again.',
    'VALIDATION_FAILED': 'Please check your request and try again.',
}

def get_user_message(error_code):
    return ERROR_MESSAGES.get(error_code, 'An unexpected error occurred. Please try again.')
```

---

For additional Device Activity API details, refer to:
- [Device Activity API](deviceActivity.md) - Complete API reference with error handling examples