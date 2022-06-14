## Tokens

### Fetch token by payment id
```py
client.payment.fetch(paymentId)
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| paymentId*    | string      | The id of the payment to be fetched |

**Response:**
```json
{
  "id": "pay_FHfqtkRzWvxky4",
  "entity": "payment",
  "amount": 100,
  "currency": "INR",
  "status": "captured",
  "order_id": "order_FHfnswDdfu96HQ",
  "invoice_id": null,
  "international": false,
  "method": "card",
  "amount_refunded": 0,
  "refund_status": null,
  "captured": true,
  "description": null,
  "card_id": "card_F0zoXUp4IPPGoI",
  "bank": null,
  "wallet": null,
  "vpa": null,
  "email": "gaurav.kumar@example.com",
  "contact": "+919876543210",
  "customer_id": "cust_DtHaBuooGHTuyZ",
  "token_id": "token_FHfn3rIiM1Z8nr",
  "notes": {
    "note_key 1": "Beam me up Scotty",
    "note_key 2": "Tea. Earl Gray. Hot."
  },
  "fee": 0,
  "tax": 0,
  "error_code": null,
  "error_description": null,
  "error_source": null,
  "error_step": null,
  "error_reason": null,
  "acquirer_data": {
    "auth_code": "541898"
  },
  "created_at": 1595449871
}
```

-------------------------------------------------------------------------------------------------------

### Fetch tokens by customer id

```py
client.token.all(customerId)
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| customerId*          | string      | The id of the customer to be fetched |

**Response:**
```json
{
  "entity": "collection",
  "count": 1,
  "items": [
    {
      "id": "token_JIskPHR6HnypUV",
      "entity": "token",
      "token": "14LDXyJ1q4MKge",
      "bank": null,
      "wallet": null,
      "method": "card",
      "card": {
        "entity": "card",
        "name": "ankit",
        "last4": "4366",
        "network": "Visa",
        "type": "credit",
        "issuer": "UTIB",
        "international": false,
        "emi": true,
        "sub_type": "consumer",
        "token_iin": null,
        "expiry_month": 12,
        "expiry_year": 2022,
        "flows": {
          "otp": true,
          "recurring": true
        }
      },
      "recurring": true,
      "recurring_details": {
        "status": "confirmed",
        "failure_reason": null
      },
      "auth_type": null,
      "mrn": null,
      "used_at": 1649861969,
      "created_at": 1649861969,
      "expired_at": 1672511399,
      "status": null,
      "notes": [],
      "dcc_enabled": false,
      "compliant_with_tokenisation_guidelines": false
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Fetch particular token
```py
client.token.fetch(customerId, tokenId)
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| customerId*          | string      | The id of the customer to be fetched |
| tokenId*          | string      | The id of the token to be fetched |

**Response:**
```json
{
  "id": "token_JIskPHR6HnypUV",
  "entity": "token",
  "token": "14LDXyJ1q4MKge",
  "bank": null,
  "wallet": null,
  "method": "card",
  "card": {
    "entity": "card",
    "name": "ankit",
    "last4": "4366",
    "network": "Visa",
    "type": "credit",
    "issuer": "UTIB",
    "international": false,
    "emi": true,
    "sub_type": "consumer",
    "token_iin": null,
    "expiry_month": 12,
    "expiry_year": 2022,
    "flows": {
      "otp": true,
      "recurring": true
    }
  },
  "recurring": true,
  "recurring_details": {
    "status": "confirmed",
    "failure_reason": null
  },
  "auth_type": null,
  "mrn": null,
  "used_at": 1649861969,
  "created_at": 1649861969,
  "expired_at": 1672511399,
  "status": null,
  "notes": [],
  "dcc_enabled": false,
  "compliant_with_tokenisation_guidelines": false
}
```
-------------------------------------------------------------------------------------------------------

### Delete token

```py
client.token.delete(customerId, tokenId)
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| customerId*          | string      | The id of the customer to be fetched |
| tokenId*          | string      | The id of the token to be fetched |

**Response:**
```json
{
    "deleted": true
}
```
-------------------------------------------------------------------------------------------------------

**PN: * indicates mandatory fields**
<br>
<br>
**For reference click [here](https://razorpay.com/docs/api/payments/recurring-payments/upi/tokens/)**