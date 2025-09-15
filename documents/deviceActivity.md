## Device Activity

### Create device activity

```py
client.device_activity.create({
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
    "type": "in_person",             # Optional: Transaction type
    "order_id": "order_R7vqkfqG3Iw02m", # Required: Order reference
    "prefill": {                     # Optional: Customer prefill data
      "name": "Gaurav Kumar",
      "email": "gaurav.kumar@example.com",
      "contact": "9000090000",
      "method": "upi"                # Optional: "upi"|"card"
    }
  }
}, device_mode="wired")
```

**Parameters:**

| Name          | Type   | Description                                                                    |
|---------------|--------|--------------------------------------------------------------------------------|
| device_id     | string | Device identifier. Required for wireless mode, optional for wired mode        |
| action*       | string | Action type. Possible values: `initiate_checkout`, `close_checkout`           |
| notes         | object | A key-value pair for additional information                                    |
| initiate_checkout* | object | Required when action is `initiate_checkout`. Contains checkout details       |
| device_mode*  | string | Device communication mode. Possible values: `wired`, `wireless`               |

**initiate_checkout Object Parameters:**

| Name          | Type   | Description                                                                    |
|---------------|--------|--------------------------------------------------------------------------------|
| name*         | string | Business name                                                                  |
| amount*       | integer| Amount in paise (₹199.00 = 19900)                                            |
| currency*     | string | Currency code (e.g., "INR")                                                   |
| description*  | string | Transaction description                                                        |
| type          | string | Optional transaction type (e.g., "in_person")                                 |
| order_id*     | string | Order reference ID                                                             |
| prefill       | object | Optional customer prefill data (name, email, contact, method)                 |

**prefill Object Parameters:**

| Name          | Type   | Description                                                                    |
|---------------|--------|--------------------------------------------------------------------------------|
| name          | string | Optional customer name                                                         |
| email         | string | Optional customer email                                                        |
| contact       | string | Optional customer contact number                                               |
| method        | string | Optional payment method: "upi", "card", "netbanking", "wallet"                |

**Success Response:**

```json
{
  "id": "pda_NVTKa9PL0yessI",
  "entity": "device.activity",
  "device_id": "2841158834",
  "action": "initiate_checkout",
  "initiate_checkout": {
    "name": "Acme Corp",
    "amount": 19900,
    "currency": "INR",
    "description": "POS Transaction",
    "order_id": "order_R7vqkfqG3Iw02m",
    "prefill": {
      "name": "Gaurav Kumar",
      "email": "gaurav.kumar@example.com",
      "contact": "9000090000",
      "method": "upi"
    }
  },
  "status": "processing",
  "error": null
}
```

**Failure Response:**

```json
{
  "id": "pda_NVTKa9PL0yessI",
  "entity": "device.activity",
  "device_id": "2841158834",
  "action": "initiate_checkout",
  "initiate_checkout": {
    "name": "Acme Corp",
    "amount": 19900,
    "currency": "INR",
    "description": "POS Transaction",
    "order_id": "order_R7vqkfqG3Iw02m",
    "prefill": {
      "name": "Gaurav Kumar",
      "email": "gaurav.kumar@example.com",
      "contact": "9000090000",
      "method": "upi"
    }
  },
  "status": "failed",
  "error": {
    "code": "BAD_REQUEST_ERROR",
    "reason": "device_not_connected"
  }
}
```

**Status Values:**
- `"processing"` - Checkout is being processed
- `"completed"` - Checkout completed successfully  
- `"failed"` - Checkout failed with error details

---

### Create device activity (Close Checkout)

```py
client.device_activity.create({
  "device_id": "2841158834",
  "action": "close_checkout"
}, device_mode="wireless")
```

**Parameters:**

| Name          | Type   | Description                                                                    |
|---------------|--------|--------------------------------------------------------------------------------|
| device_id     | string | Device identifier. Required for wireless mode, optional for wired mode        |
| action*       | string | Action type: `close_checkout`                                                  |
| device_mode*  | string | Device communication mode. Possible values: `wired`, `wireless`               |

**Success Response:**

```json
{
  "id": "pda_NVTKa9PL0yessJ",
  "entity": "device.activity", 
  "device_id": "2841158834",
  "action": "close_checkout",
  "status": "completed",
  "error": null
}
```

**Failure Response:**

```json
{
  "id": "pda_NVTKa9PL0yessJ",
  "entity": "device.activity",
  "device_id": "2841158834",
  "action": "close_checkout",
  "status": "failed",
  "error": {
    "code": "BAD_REQUEST_ERROR",
    "reason": "checkout_not_found"
  }
}
```
---

## Device Modes

### Wired Mode
- **device_mode**: `"wired"`
- **device_id**: Optional
- Direct device connection

### Wireless Mode  
- **device_mode**: `"wireless"`
- **device_id**: Required
- Wireless device communication

---

## Error Handling

```py
from razorpay.errors import BadRequestError

try:
    response = client.device_activity.create({
        "device_id": "2841158834",
        "action": "initiate_checkout"
    }, device_mode="invalid_mode")
except BadRequestError as e:
    print(f"Error: {e}")
    # Output: Invalid device mode. Allowed values are 'wired' and 'wireless'.
```

**Common Errors:**

| Error | Description | Solution |
|-------|-------------|----------|
| `BadRequestError` | Invalid device_mode parameter | Use only `"wired"` or `"wireless"` |
| `BadRequestError` | Missing activity_id | Provide valid activity ID for get_status |
| `BadRequestError` | Missing device_id in wireless mode | Include device_id when using wireless mode |

**API Error Responses:**

| Error Code | Reason | Description | Solution |
|------------|--------|-------------|----------|
| `BAD_REQUEST_ERROR` | `device_not_connected` | Device is not connected | Check device connection and try again |
| `BAD_REQUEST_ERROR` | `checkout_not_found` | Checkout session not found | Verify checkout was initiated before closing |

---

## Example Usage

```py
import razorpay

# Initialize client
client = razorpay.Client(auth=('key_id', 'key_secret'), base_url='http://localhost:PORT')

try:
    # Step 1: Initiate checkout
    activity = client.device_activity.create({
        "device_id": "2841158834",
        "action": "initiate_checkout",
        "notes": {"merchant_id": "12345"},
        "initiate_checkout": {
            "name": "Acme Corp",
            "amount": 19900,
            "currency": "INR",
            "description": "POS Transaction",
            "type": "in_person",             # Optional
            "order_id": "order_R7vqkfqG3Iw02m",
            "prefill": {
                "name": "Gaurav Kumar",
                "email": "gaurav.kumar@example.com",
                "contact": "9000090000",
                "method": "upi"
            }
        }
    }, device_mode="wired")
    
    activity_id = activity['id']
    print(f"Checkout initiated: {activity_id}")
    
    # Step 2: Check status
    status = client.device_activity.get_status(activity_id, device_mode="wired")
    print(f"Current status: {status['status']}")
    
    # Step 3: Close checkout when done
    close_response = client.device_activity.create({
        "device_id": "2841158834", 
        "action": "close_checkout"
    }, device_mode="wired")
    
    print("Checkout closed successfully")

except Exception as e:
    print(f"Error: {e}")
```

---

## Integration with Order APIs

Device Activity APIs work seamlessly with Order APIs for complete POS integration:

```py
# Create order with device_mode
order = client.order.create({
    "amount": 50000,
    "currency": "INR",
    "receipt": "order_001"
}, device_mode="wired")

# Initiate device checkout
checkout = client.device_activity.create({
    "device_id": "2841158834",
    "action": "initiate_checkout",
    "notes": {"order_id": order['id']},
    "initiate_checkout": {
        "name": "Acme Corp",
        "amount": order['amount'],
        "currency": order['currency'],
        "description": "POS Transaction",
        "type": "in_person",
        "order_id": order['id'],
        "prefill": {
            "method": "upi"
        }
    }
}, device_mode="wired")

# Monitor checkout status  
status = client.device_activity.get_status(checkout['id'], device_mode="wired")
``` 