## Payments

### Capture payment

```py
client.payment.capture(paymentId,{
  "amount" : 1000,
  "currency" : "INR"
})
```

**Parameters:**

| Name      | Type    | Description                                                                    |
|-----------|---------|--------------------------------------------------------------------------------|
| paymentId* | string  | Id of the payment to capture                                                   |
| amount*    | integer | The amount to be captured (should be equal to the authorized amount, in paise) |
| currency   | string  | The currency of the payment (defaults to INR)                                  |

**Response:**
```json
{
  "id": "pay_G8VQzjPLoAvm6D",
  "entity": "payment",
  "amount": 1000,
  "currency": "INR",
  "status": "captured",
  "order_id": "order_G8VPOayFxWEU28",
  "invoice_id": null,
  "international": false,
  "method": "upi",
  "amount_refunded": 0,
  "refund_status": null,
  "captured": true,
  "description": "Purchase Shoes",
  "card_id": null,
  "bank": null,
  "wallet": null,
  "vpa": "gaurav.kumar@exampleupi",
  "email": "gaurav.kumar@example.com",
  "contact": "+919999999999",
  "customer_id": "cust_DitrYCFtCIokBO",
  "notes": [],
  "fee": 24,
  "tax": 4,
  "error_code": null,
  "error_description": null,
  "error_source": null,
  "error_step": null,
  "error_reason": null,
  "acquirer_data": {
    "rrn": "033814379298"
  },
  "created_at": 1606985209
}
```
-------------------------------------------------------------------------------------------------------

### Fetch all payments

```py
client.payment.all(option)
```

**Parameters:**

| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| from  | timestamp | timestamp after which the payments were created  |
| to    | timestamp | timestamp before which the payments were created |
| count | integer   | number of payments to fetch (default: 10)        |
| skip  | integer   | number of payments to be skipped (default: 0)    |

**Response:**
```json
{
  "entity": "collection",
  "count": 2,
  "items": [
    {
      "id": "pay_G8VaL2Z68LRtDs",
      "entity": "payment",
      "amount": 900,
      "currency": "INR",
      "status": "captured",
      "order_id": "order_G8VXfKDWDEOHHd",
      "invoice_id": null,
      "international": false,
      "method": "netbanking",
      "amount_refunded": 0,
      "refund_status": null,
      "captured": true,
      "description": "Purchase Shoes",
      "card_id": null,
      "bank": "KKBK",
      "wallet": null,
      "vpa": null,
      "email": "gaurav.kumar@example.com",
      "contact": "+919999999999",
      "customer_id": "cust_DitrYCFtCIokBO",
      "notes": [],
      "fee": 22,
      "tax": 4,
      "error_code": null,
      "error_description": null,
      "error_source": null,
      "error_step": null,
      "error_reason": null,
      "acquirer_data": {
        "bank_transaction_id": "0125836177"
      },
      "created_at": 1606985740
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Fetch a payment

```py
client.payment.fetch(paymentId)
```

**Parameters:**

| Name       | Type   | Description                       |
|------------|--------|-----------------------------------|
| paymentId* | string | Id of the payment to be retrieved |

**Response:**
```json
{
  "id": "pay_G8VQzjPLoAvm6D",
  "entity": "payment",
  "amount": 1000,
  "currency": "INR",
  "status": "captured",
  "order_id": "order_G8VPOayFxWEU28",
  "invoice_id": null,
  "international": false,
  "method": "upi",
  "amount_refunded": 0,
  "refund_status": null,
  "captured": true,
  "description": "Purchase Shoes",
  "card_id": null,
  "bank": null,
  "wallet": null,
  "vpa": "gaurav.kumar@exampleupi",
  "email": "gaurav.kumar@example.com",
  "contact": "+919999999999",
  "customer_id": "cust_DitrYCFtCIokBO",
  "notes": [],
  "fee": 24,
  "tax": 4,
  "error_code": null,
  "error_description": null,
  "error_source": null,
  "error_step": null,
  "error_reason": null,
  "acquirer_data": {
    "rrn": "033814379298"
  },
  "created_at": 1606985209
}
```
-------------------------------------------------------------------------------------------------------

### Fetch payments for an order

```py
client.order.payment(orderId)
```
**Parameters**

| Name     | Type   | Description                         |
|----------|--------|-------------------------------------|
| orderId* | string | The id of the order to be retrieve payment info |

**Response:**
```json
{
  "count": 1,
  "entity": "collection",
  "items": [
    {
      "id": "pay_DovGQXOkPBJjjU",
      "entity": "payment",
      "amount": 600,
      "currency": "INR",
      "status": "captured",
      "order_id": "order_DovFx48wjYEr2I",
      "method": "netbanking",
      "amount_refunded": 0,
      "refund_status": null,
      "captured": true,
      "description": "A Wild Sheep Chase is a novel by Japanese author Haruki Murakami",
      "card_id": null,
      "bank": "SBIN",
      "wallet": null,
      "vpa": null,
      "email": "gaurav.kumar@example.com",
      "contact": "9364591752",
      "fee": 70,
      "tax": 10,
      "error_code": null,
      "error_description": null,
      "error_source": null,
      "error_step": null,
      "error_reason": null,
      "notes": [],
      "acquirer_data": {
        "bank_transaction_id": "0125836177"
      },
      "created_at": 1400826750
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Update a payment

```py
client.payment.edit(paymentId,{
	"notes": {
		"key1": "value1",
		"key2": "value2"
	}
})
```

**Parameters:**

| Name        | Type    | Description                          |
|-------------|---------|--------------------------------------|
| paymentId* | string  | Id of the payment to update          |
| notes*       | object  | A key-value pair                     |

**Response:**
```json
{
  "id": "pay_CBYy6tLmJTzn3Q",
  "entity": "payment",
  "amount": 1000,
  "currency": "INR",
  "status": "authorized",
  "order_id": null,
  "invoice_id": null,
  "international": false,
  "method": "netbanking",
  "amount_refunded": 0,
  "refund_status": null,
  "captured": false,
  "description": null,
  "card_id": null,
  "bank": "UTIB",
  "wallet": null,
  "vpa": null,
  "email": "testme@acme.com",
  "notes": {
    "key1": "value1",
    "key2": "value2"
  },
  "fee": null,
  "tax": null,
  "error_code": null,
  "error_description": null,
  "error_source": null,
  "error_step": null,
  "error_reason": null,
  "acquirer_data": {
    "bank_transaction_id": "0125836177"
  },
  "created_at": 1553504328
}
```
-------------------------------------------------------------------------------------------------------

### Fetch expanded card or emi details for payments

Request #1: Card

```py
client.payment.all({'expand[]':'card'})
```

Request #2: EMI

```py
client.payment.all({'expand[]':'emi'})
```

**Response:**<br>
For expanded card or emi details for payments response please click [here](https://razorpay.com/docs/api/payments/#fetch-expanded-card-or-emi-details-for-payments)

-------------------------------------------------------------------------------------------------------

### Fetch card details with paymentId

```py
client.payment.fetchCardDetails(paymentId)
```

**Parameters:**

| Name        | Type    | Description                          |
|-------------|---------|--------------------------------------|
| paymentId* | string  | Id of the payment to update          |

**Response:**
```json
{
  "id": "card_6krZ6bcjoeqyV9",
  "entity": "card",
  "name": "Gaurav",
  "last4": "3335",
  "network": "Visa",
  "type": "debit",
  "issuer": "SBIN",
  "international": false,
  "emi": null,
  "sub_type": "business"
}
```
-------------------------------------------------------------------------------------------------------

### Fetch Payment Downtime Details

```py
client.payment.fetchPaymentDowntime()
```
**Response:** <br>
For payment downtime response please click [here](https://razorpay.com/docs/api/payments/downtime/#fetch-payment-downtime-details)

-------------------------------------------------------------------------------------------------------

### Fetch Payment Downtime

```py
client.payment.fetchPaymentDowntimeById(downtimeId)
```

**Parameters:**

| Name        | Type    | Description                          |
|-------------|---------|--------------------------------------|
| downtimeId* | string  | Id to fetch payment downtime         |

**Response:**
For payment downtime by id response please click [here](https://razorpay.com/docs/api/payments/downtime/#fetch-payment-downtime-details-by-id)
-------------------------------------------------------------------------------------------------------

### Payment capture settings API

```py
client.order.create({
  'amount':50000,
  'currency': 'INR',
  'receipt': 'rcptid_11',
  'payment': {
    'capture': 'automatic',
    'capture_options': {
      'automatic_expiry_period': 12,
      'manual_expiry_period': 7200,
      'refund_speed': 'optimum'
    }  
  }
})
```

**Parameters:**

| Name        | Type    | Description                          |
|-------------|---------|--------------------------------------|
| amount*          | integer | Amount of the order to be paid                                               |
| currency*        | string  | Currency of the order. Currently only `INR` is supported.       |
| receipt         | string  | Your system order reference id.                                              |
| payment         | object  | please refer this [doc](https://razorpay.com/docs/payments/payments/capture-settings/api/) for params                       |

**Response:** <br>
```json
{
  "id": "order_DBJOWzybf0sJbb",
  "entity": "order",
  "amount": 50000,
  "amount_paid": 0,
  "amount_due": 50000,
  "currency": "INR",
  "receipt": "rcptid_11",
  "status": "created",
  "attempts": 0,
  "notes": [],
  "created_at": 1566986570
}
```
-------------------------------------------------------------------------------------------------------

### Create Payment Json

```py
client.payment.createPaymentJson({
  "amount": 100,
  "currency": "INR",
  "order_id": "order_EAkbvXiCJlwhHR",
  "email": "gaurav.kumar@example.com",
  "contact": 9090909090,
  "method": "card",
  "card":{
    "number": 4111111111111111,
    "name": "Gaurav",
    "expiry_month": 11,
    "expiry_year": 23,
    "cvv": 100
  }
})
```

**Parameters:**
 please refer this [doc](https://razorpay.com/docs/payment-gateway/s2s-integration/payment-methods/) for params

**Response:** <br>
```json
{
  "razorpay_payment_id": "pay_FVmAstJWfsD3SO",
  "next": [
    {
      "action": "redirect",
      "url": "https://api.razorpay.com/v1/payments/FVmAtLUe9XZSGM/authorize"
    },
    {
      "action": "otp_generate",
      "url": "https://api.razorpay.com/v1/payments/pay_FVmAstJWfsD3SO/otp_generate?track_id=FVmAtLUe9XZSGM&key_id=<YOUR_KEY_ID>"
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Create Payment Json (Third party validation)

```py
client.payment.createPaymentJson({
  "amount": "500",
  "currency": "INR",
  "email": "gaurav.kumar@example.com",
  "contact": "9123456789",
  "order_id": "order_GAWN9beXgaqRyO",
  "method": "netbanking",
  "bank": "HDFC"
})
```

**Parameters:**
| Name        | Type    | Description                          |
|-------------|---------|--------------------------------------|
| amount*          | integer | Amount of the order to be paid  |
| currency*   | string  | The currency of the payment (defaults to INR)                                  |
| order_id*        | string  | The unique identifier of the order created. |
| email*        | string      | Email of the customer                       |
| contact*      | string      | Contact number of the customer              |
| method*      | string  | Possible value is `netbanking` |
| bank      | string      | The customer's bank code.For example, `HDFC`.|

 please refer this [doc](https://razorpay.com/docs/payments/third-party-validation/s2s-integration/netbanking#step-3-create-a-payment) for params

**Response:** <br>
```json
{
  "razorpay_payment_id": "pay_GAWOYqPlvrtPSi",
  "next": [
    {
      "action": "redirect",
      "url": "https://api.razorpay.com/v1/payments/pay_GAWOYqPlvrtPSi/authorize"
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------
### Create Payment UPI s2s / VPA token (Third party validation)

```py
client.payment.createUpi({
  "amount": 200,
  "currency": "INR",
  "order_id": "order_GAWRjlWkVcRh0V",
  "email": "gaurav.kumar@example.com",
  "contact": "9123456789",
  "method": "upi",
  "customer_id": "cust_EIW4T2etiweBmG",
  "save": 1,
  "ip": "192.168.0.103",
  "referer": "http",
  "user_agent": "Mozilla/5.0",
  "description": "Test flow",
  "notes": {
    "note_key": "value1"
  },
  "upi": {
    "flow": "collect",
    "vpa": "gauravkumar@exampleupi",
    "expiry_time": 5
  }
})
```

**Parameters:**
| Name        | Type    | Description                          |
|-------------|---------|--------------------------------------|
| amount*          | integer | Amount of the order to be paid  |
| currency*   | string  | The currency of the payment (defaults to INR)                                  |
| order_id*        | string  | The unique identifier of the order created. |
| email*        | string      | Email of the customer                       |
| customer_id*   | string      | The id of the customer to be fetched |
| contact*      | string      | Contact number of the customer              |
| notes | array  | A key-value pair  |
| description | string  | Descriptive text of the payment. |
| save | boolean  |  Specifies if the VPA should be stored as tokens.Possible value is `0`, `1`  |
| callback_url   | string      | URL where Razorpay will submit the final payment status. |
| ip*   | string      | The client's browser IP address. For example `117.217.74.98` |
| referer*   | string      | Value of `referer` header passed by the client's browser. For example, `https://example.com/` |
| user_agent*   | string      | Value of `user_agent` header passed by the client's browser. For example, `Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36` |
| upi* (for Upi only)  | array      | All keys listed [here](https://razorpay.com/docs/payments/third-party-validation/s2s-integration/upi/collect#step-14-initiate-a-payment) are supported  |

**Response:** <br>
```json
{
  "razorpay_payment_id": "pay_EAm09NKReXi2e0"
}
```
-------------------------------------------------------------------------------------------------------
### Create Payment UPI s2s / VPA token (Third party validation)

```py
client.payment.createUpi({
    "amount": 100,
    "currency": "INR",
    "order_id": "order_Ee0biRtLOqzRjP",
    "email": "gaurav.kumar@example.com",
    "contact": "9090909090",
    "method": "upi",
    "ip": "192.168.0.103",
    "referer": "http",
    "user_agent": "Mozilla/5.0",
    "description": "Test flow",
    "notes": {
      "purpose": "UPI test payment"
    },
    "upi": {
      "flow" : "intent"
    }
})
```

**Parameters:**
| Name        | Type    | Description                          |
|-------------|---------|--------------------------------------|
| amount*          | integer | Amount of the order to be paid  |
| currency*   | string  | The currency of the payment (defaults to INR)                                  |
| order_id*        | string  | The unique identifier of the order created. |
| email*        | string      | Email of the customer                       |
| customer_id*   | string      | The id of the customer to be fetched |
| contact*      | string      | Contact number of the customer              |
| notes | array  | A key-value pair  |
| description | string  | Descriptive text of the payment. |
| save | boolean  |  Specifies if the VPA should be stored as tokens.Possible value is `0`, `1`  |
| callback_url   | string      | URL where Razorpay will submit the final payment status. |
| ip*   | string      | The client's browser IP address. For example `117.217.74.98` |
| referer*   | string      | Value of `referer` header passed by the client's browser. For example, `https://example.com/` |
| user_agent*   | string      | Value of `user_agent` header passed by the client's browser. For example, `Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36` |
| upi* (for Upi only)  | array      | All keys listed [here](https://razorpay.com/docs/payments/third-party-validation/s2s-integration/upi/intent/#step-2-initiate-a-payment) are supported  |

**Response:** <br>
```json
{
  "razorpay_payment_id": "pay_CMeM6XvOPGFiF",
  "link": "upi://pay?pa=success@razorpay&pn=xyz&tr=xxxxxxxxxxx&tn=gourav&am=1&cu=INR&mc=xyzw"
}
```
-------------------------------------------------------------------------------------------------------

### Valid VPA (Third party validation)

```py
client.payment.validateVpa({
  "vpa": "gauravkumar@exampleupi"
})
```

**Parameters:**
| Name        | Type    | Description                          |
|-------------|---------|--------------------------------------|
| vpa*          | string | The virtual payment address (VPA) you want to validate. For example,   `gauravkumar@exampleupi`  |

 please refer this [doc](https://razorpay.com/docs/payments/third-party-validation/s2s-integration/upi/collect#step-13-validate-the-vpa) for params

**Response:** <br>
```json
{
  "vpa": "gauravkumar@exampleupi",
  "success": true,
  "customer_name": "Gaurav Kumar"
}
```
-------------------------------------------------------------------------------------------------------

### Fetch payment methods (Third party validation)

```py
client = razorpay.Client(auth=("key", "")) // Use Only razorpay key
client.payment.fetchPaymentMethods()
```

**Response:** <br>
 please refer this [doc](https://razorpay.com/docs/payments/third-party-validation/s2s-integration/methods-api/#fetch-payment-methods) for response

```
-------------------------------------------------------------------------------------------------------

**PN: * indicates mandatory fields**
<br>
<br>
**For reference click [here](https://razorpay.com/docs/api/payments/)**