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

### 1. Device Activity Management

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
        "name": "Acme Corp",             # Required: Business name
        "amount": 19900,                 # Required: Amount in paise (₹199.00)
        "currency": "INR",               # Required: Currency code
        "description": "POS Transaction", # Required: Transaction description
        "type": "in_person",             # Required: Transaction type
        "order_id": "order_R7vqkfqG3Iw02m", # Required: Order reference
        "method": "upi",                 # Required: "upi"|"card"|"netbanking"|"wallet"
        "prefill": {                     # Optional: Customer prefill data
            "name": "Gaurav Kumar",
            "email": "gaurav.kumar@example.com",
            "contact": "9000090000"
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

#### Check Activity Status

```py
response = client.device_activity.get_status(
    "act_12345678",         # Required: Activity ID from create response
    device_mode="wired"     # Required: "wired" or "wireless"
)
```

### 2. Order Management

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

---

## Device Modes

| Mode | Description | device_id Required |
|------|-------------|-------------------|
| **wired** | Direct device connection | ✅ Yes |
| **wireless** | Wireless communication | ❌ Optional |

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
                    "type": "in_person",
                    "order_id": order['id'],
                    "method": "upi",
                    "prefill": {
                        "name": "Customer Name",
                        "email": "customer@example.com",
                        "contact": "9000090000"
                    }
                }
            }, device_mode=device_mode)
            
            activity_id = activity['id']
            print(f"Checkout initiated: {activity_id}")
            
            # Step 3: Monitor Status (polling example)
            max_attempts = 30  # 5 minutes max
            for attempt in range(max_attempts):
                try:
                    status = self.client.device_activity.get_status(activity_id, device_mode=device_mode)
                    current_status = status['status']
                    
                    print(f"Status check {attempt + 1}: {current_status}")
                    
                    if current_status == 'completed':
                        # Step 4: Get final order details with payments
                        order_with_payments = self.client.order.fetch(
                            order['id'], 
                            data={"expand[]": "payments"}, 
                            device_mode=device_mode
                        )
                        
                        return {
                            "success": True,
                            "order": order_with_payments,
                            "activity": status
                        }
                    
                    elif current_status == 'failed':
                        error_details = status.get('error', {})
                        return {
                            "success": False,
                            "error": f"Checkout failed: {error_details.get('code')} - {error_details.get('reason')}",
                            "activity": status
                        }
                    
                    time.sleep(10)  # Wait 10 seconds before next check
                    
                except Exception as e:
                    print(f"Status check failed: {e}")
                    continue
            
            # Timeout - close checkout
            self.close_checkout(device_mode=device_mode)
            return {
                "success": False,
                "error": "Checkout timeout"
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

## Authentication

### Device Activity APIs
- **Type**: Public Authentication (key_id only)
- **Usage**: Automatically handled by SDK
- **Security**: More secure for device operations

### Order APIs  
- **Type**: Standard Authentication (key_id + key_secret)
- **Usage**: Automatically handled by SDK
- **Security**: Full authentication for payment operations

---

## Error Handling

```py
from razorpay.errors import BadRequestError

try:
    response = client.device_activity.create(data, device_mode="wired")
except BadRequestError as e:
    if "Invalid device mode" in str(e):
        print("Use 'wired' or 'wireless' for device_mode")
    elif "Activity ID must be provided" in str(e):
        print("Provide valid activity_id for get_status")
    else:
        print(f"API Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

**Common Error Solutions:**

| Error | Cause | Solution |
|-------|-------|----------|
| `Invalid device mode` | Wrong device_mode value | Use `"wired"` or `"wireless"` |
| `Activity ID must be provided` | Missing activity_id | Provide valid activity ID |
| `device_id required for wired mode` | Missing device_id | Include device_id for wired mode |

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
| `get_status()` | `activity_id`, `device_mode` | Activity status | Check activity status |

**Usage Examples:**
```py
# Initiate checkout
activity = client.device_activity.create(data, device_mode="wired")

# Check status  
status = client.device_activity.get_status("pda_123", device_mode="wired")

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

For additional Device Activity API details, refer to:
- [Device Activity API](deviceActivity.md) - Complete API reference with error handling examples