## Transfers

### Create transfers from payment

```py
client.payment.fetch(paymentId,{
   "transfers": [
    {
      "account": 'acc_HgzcrXeSLfNP9U',
      "amount": 100,
      "currency": "INR",
      "notes": {
        "name": "Gaurav Kumar",
        "roll_no": "IEC2011025"
      },
      "linked_account_notes": [
        "branch"
      ],
      "on_hold": True,
      "on_hold_until": 1671222870
    }
  ]
 })
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| paymentId*   | string      | The id of the payment to be fetched  |
| transfers   | object     | All parameters listed [here](https://razorpay.com/docs/api/route/#create-transfers-from-payments) are supported |

**Response:**
```json
{
  "id": "pay_DJiaO3iqUZaZrO",
  "entity": "payment",
  "amount": 5000,
  "currency": "INR",
  "status": "captured",
  "order_id": null,
  "invoice_id": null,
  "international": false,
  "method": "netbanking",
  "amount_refunded": 0,
  "refund_status": null,
  "captured": true,
  "description": "Credits towards consultation",
  "card_id": null,
  "bank": "UTIB",
  "wallet": null,
  "vpa": null,
  "email": "void@razorpay.com",
  "contact": "+919191919191",
  "notes": [],
  "fee": 171,
  "tax": 26,
  "error_code": null,
  "error_description": null,
  "error_source": null,
  "error_step": null,
  "error_reason": null,
  "acquirer_data": {
    "bank_transaction_id": "7909502"
  },
  "created_at": 1568822005
}
```
-------------------------------------------------------------------------------------------------------

### Create transfers from order

```py
client.order.create({
  "amount": 2000,
  "currency": "INR",
  "transfers": [
    {
      "account": "acc_CPRsN1LkFccllA",
      "amount": 1000,
      "currency": "INR",
      "notes": {
        "branch": "Acme Corp Bangalore North",
        "name": "Gaurav Kumar"
      },
      "linked_account_notes": [
        "branch"
      ],
      "on_hold": True,
      "on_hold_until": 1671222870
    },
    {
      "account": "acc_CNo3jSI8OkFJJJ",
      "amount": 1000,
      "currency": "INR",
      "notes": {
        "branch": "Acme Corp Bangalore South",
        "name": "Saurav Kumar"
      },
      "linked_account_notes": [
        "branch"
      ],
      "on_hold": True
    }
  ]
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| amount*   | integer      | The transaction amount, in paise |
| currency*   | string  | The currency of the payment (defaults to INR)  |
|  receipt      | string      | A unique identifier provided by you for your internal reference. |
| transfers   | object     | All parameters listed [here](https://razorpay.com/docs/api/route/#create-transfers-from-orders) are supported |

**Response:**
```json
{
  "id": "order_E9uTczH8uWPCyQ",
  "entity": "order",
  "amount": 2000,
  "amount_paid": 0,
  "amount_due": 2000,
  "currency": "INR",
  "receipt": null,
  "offer_id": null,
  "status": "created",
  "attempts": 0,
  "notes": [],
  "created_at": 1580217565,
  "transfers": [
    {
      "recipient": "acc_CPRsN1LkFccllA",
      "amount": 1000,
      "currency": "INR",
      "notes": {
        "branch": "Acme Corp Bangalore North",
        "name": "Gaurav Kumar"
      },
      "linked_account_notes": [
        "branch"
      ],
      "on_hold": true,
      "on_hold_until": 1671222870
    },
    {
      "recipient": "acc_CNo3jSI8OkFJJJ",
      "amount": 1000,
      "currency": "INR",
      "notes": {
        "branch": "Acme Corp Bangalore South",
        "name": "Saurav Kumar"
      },
      "linked_account_notes": [
        "branch"
      ],
      "on_hold": false,
      "on_hold_until": null
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Direct transfers

```py
client.transfer.create({
  "account": accountId,
  "amount": 500,
  "currency": "INR"
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| accountId*   | string      | The id of the account to be fetched  |
| amount*   | integer      | The amount to be captured (should be equal to the authorized amount, in paise) |
| currency*   | string  | The currency of the payment (defaults to INR)  |

**Response:**
```json
{
  "id": "trf_JnRRvcSbZb1VHN",
  "entity": "transfer",
  "status": "processed",
  "source": "acc_HZbJUcl6DBDLIN",
  "recipient": "acc_HjVXbtpSCIxENR",
  "amount": 500,
  "currency": "INR",
  "amount_reversed": 0,
  "fees": 1,
  "tax": 0,
  "notes": [],
  "linked_account_notes": [],
  "on_hold": false,
  "on_hold_until": null,
  "recipient_settlement_id": null,
  "created_at": 1656534379,
  "processed_at": 1656534379,
  "error": {
    "code": null,
    "description": null,
    "reason": null,
    "field": null,
    "step": null,
    "id": "trf_JnRRvcSbZb1VHN",
    "source": null,
    "metadata": null
  }
}
```
-------------------------------------------------------------------------------------------------------

### Fetch transfer for a payment

```py
client.payment.transfers(paymentId)
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| paymentId*   | string      | The id of the payment to be fetched  |

**Response:**
```json
{
  "entity": "collection",
  "count": 1,
  "items": [
    {
      "id": "trf_I8kA5qRv9czK3Y",
      "entity": "transfer",
      "status": "processed",
      "source": "pay_I7watngocuEY4P",
      "recipient": "acc_HjVXbtpSCIxENR",
      "amount": 10000,
      "currency": "INR",
      "amount_reversed": 0,
      "fees": 12,
      "tax": 2,
      "notes": [],
      "linked_account_notes": [],
      "on_hold": false,
      "on_hold_until": null,
      "settlement_status": "pending",
      "recipient_settlement_id": null,
      "created_at": 1634111246,
      "processed_at": 1634111251,
      "error": {
        "code": null,
        "description": null,
        "reason": null,
        "field": null,
        "step": null,
        "id": "trf_I8kA5qRv9czK3Y",
        "source": null,
        "metadata": null
      }
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Fetch transfer for an order

```py
client.order.fetch(orderId, {
  "expand[]": "transfers"
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| orderId*   | string      | The id of the order to be fetched  |
| expand[]*   | string    | Supported value is `transfer`  |

**Response:**
```json
{
  "id": "order_I7waiV9PUGADuv",
  "entity": "order",
  "amount": 50000,
  "amount_paid": 50000,
  "amount_due": 0,
  "currency": "INR",
  "receipt": "55",
  "offer_id": null,
  "status": "paid",
  "attempts": 1,
  "notes": {
    "woocommerce_order_number": "55"
  },
  "created_at": 1633936677,
  "transfers": {
    "entity": "collection",
    "count": 1,
    "items": [
      {
        "id": "trf_I7waiajxgS5jWL",
        "entity": "transfer",
        "status": "processed",
        "source": "order_I7waiV9PUGADuv",
        "recipient": "acc_HalyQGZh9ZyiGg",
        "amount": 10000,
        "currency": "INR",
        "amount_reversed": 0,
        "fees": 12,
        "tax": 2,
        "notes": [],
        "linked_account_notes": [],
        "on_hold": false,
        "on_hold_until": null,
        "settlement_status": "pending",
        "recipient_settlement_id": null,
        "created_at": 1633936677,
        "processed_at": 1633936700,
        "error": {
          "code": null,
          "description": null,
          "reason": null,
          "field": null,
          "step": null,
          "id": "trf_I7waiajxgS5jWL",
          "source": null,
          "metadata": null
        }
      }
    ]
  }
}
```
-------------------------------------------------------------------------------------------------------

### Fetch transfer

```py
client.transfer.fetch(transferId)
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| transferId*   | string      | The id of the transfer to be fetched  |

**Response:**
```json
{
  "id": "trf_I7waiajxgS5jWL",
  "entity": "transfer",
  "status": "processed",
  "source": "order_I7waiV9PUGADuv",
  "recipient": "acc_HalyQGZh9ZyiGg",
  "amount": 10000,
  "currency": "INR",
  "amount_reversed": 0,
  "fees": 12,
  "tax": 2,
  "notes": [],
  "linked_account_notes": [],
  "on_hold": false,
  "on_hold_until": null,
  "settlement_status": "pending",
  "recipient_settlement_id": null,
  "created_at": 1633936677,
  "processed_at": 1633936700,
  "error": {
    "code": null,
    "description": null,
    "reason": null,
    "field": null,
    "step": null,
    "id": "trf_I7waiajxgS5jWL",
    "source": null,
    "metadata": null
  }
}
```
-------------------------------------------------------------------------------------------------------

### Fetch transfers for a settlement

```py
client.transfer.all({
   "recipient_settlement_id" :  recipientSettlementId
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| recipientSettlementId*   | string    | The recipient settlement id obtained from the settlement.processed webhook payload.  |

**Response:**
```json
{
  "entity": "collection",
  "count": 1,
  "items": [
    {
      "id": "trf_HWjmkReRGPhguR",
      "entity": "transfer",
      "status": "processed",
      "source": "pay_HWjY9DZSMsbm5E",
      "recipient": "acc_HWjl1kqobJzf4i",
      "amount": 1000,
      "currency": "INR",
      "amount_reversed": 0,
      "fees": 3,
      "tax": 0,
      "notes": [],
      "linked_account_notes": [],
      "on_hold": false,
      "on_hold_until": null,
      "settlement_status": "settled",
      "recipient_settlement_id": "setl_HYIIk3H0J4PYdX",
      "created_at": 1625812996,
      "processed_at": 1625812996,
      "error": {
        "code": null,
        "description": null,
        "reason": null,
        "field": null,
        "step": null,
        "id": "trf_HWjmkReRGPhguR",
        "source": null,
        "metadata": null
      }
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Fetch settlement details

```py
client.transfer.all({
  'expand[]':'recipient_settlement'  
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| expand*   | string    | Supported value is `recipient_settlement`  |

**Response:**
```json
{
  "entity": "collection",
  "count": 1,
  "items": [
    {
      "id": "trf_JnRRvcSbZb1VHN",
      "entity": "transfer",
      "status": "processed",
      "source": "acc_HZbJUcl6DBDLIN",
      "recipient": "acc_HjVXbtpSCIxENR",
      "amount": 500,
      "currency": "INR",
      "amount_reversed": 0,
      "fees": 1,
      "tax": 0,
      "notes": [],
      "linked_account_notes": [],
      "on_hold": false,
      "on_hold_until": null,
      "settlement_status": null,
      "recipient_settlement_id": null,
      "recipient_settlement": null,
      "created_at": 1656534379,
      "processed_at": 1656534379,
      "error": {
        "code": null,
        "description": null,
        "reason": null,
        "field": null,
        "step": null,
        "id": "trf_JnRRvcSbZb1VHN",
        "source": null,
        "metadata": null
      }
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Refund payments and reverse transfer from a linked account

```py
client.payment.refund(paymentId,{
    "amount" : 100,
    "reverse_all" : True
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| paymentId*   | string      | The id of the payment to be fetched  |
| amount*   | integer      | The amount to be captured (should be equal to the authorized amount, in paise) |
| reverse_all   | boolean    | Reverses transfer made to a linked account. Possible values:<br> * `True` - Reverses transfer made to a linked account.<br>* `False` - Does not reverse transfer made to a linked account.|

**Response:**
```json
{
  "id": "rfnd_JJFNlNXPHY640A",
  "entity": "refund",
  "amount": 100,
  "currency": "INR",
  "payment_id": "pay_JJCqynf4fQS0N1",
  "notes": [],
  "receipt": null,
  "acquirer_data": {
    "arn": null
  },
  "created_at": 1649941680,
  "batch_id": null,
  "status": "processed",
  "speed_processed": "normal",
  "speed_requested": "normal"
}
```
-------------------------------------------------------------------------------------------------------

### Fetch payments of a linked account

```py
client.payment.all({
  'X-Razorpay-Account':  linkedAccountId
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| X-Razorpay-Account   | string      | The linked account id to fetch the payments received by linked account |

**Response:**
```json
{
  "entity": "collection",
  "count": 2,
  "items": [
    {
      "id": "pay_JJCqynf4fQS0N1",
      "entity": "payment",
      "amount": 10000,
      "currency": "INR",
      "status": "captured",
      "order_id": "order_JJCqnZG8f3754z",
      "invoice_id": null,
      "international": false,
      "method": "netbanking",
      "amount_refunded": 0,
      "refund_status": null,
      "captured": true,
      "description": "#JJCqaOhFihfkVE",
      "card_id": null,
      "bank": "YESB",
      "wallet": null,
      "vpa": null,
      "email": "john.example@example.com",
      "contact": "+919820958250",
      "notes": [],
      "fee": 236,
      "tax": 36,
      "error_code": null,
      "error_description": null,
      "error_source": null,
      "error_step": null,
      "error_reason": null,
      "acquirer_data": {
        "bank_transaction_id": "2118867"
      },
      "created_at": 1649932775
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Reverse transfers from all linked accounts

```py
client.transfer.reverse(transferId,{
    "amount":100
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| transferId*   | string      | The id of the transfer to be fetched  |
| amount   | integer      | The amount to be captured (should be equal to the authorized amount, in paise) |

**Response:**
```json
{
  "id": "rfnd_JJFNlNXPHY640A",
  "entity": "refund",
  "amount": 100,
  "currency": "INR",
  "payment_id": "pay_JJCqynf4fQS0N1",
  "notes": [],
  "receipt": null,
  "acquirer_data": {
    "arn": null
  },
  "created_at": 1649941680,
  "batch_id": null,
  "status": "processed",
  "speed_processed": "normal",
  "speed_requested": "normal"
}
```
-------------------------------------------------------------------------------------------------------

### Hold settlements for transfers
```py
paymentId = "pay_00000000000001"

client.payment.transfer(paymentId,{
  "transfers": [
    {
      "amount": 100,
      "account": "acc_CMaomTz4o0FOFz",
      "currency": "INR",
      "on_hold": True
    }
  ]
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| paymentId*   | string      | The id of the payment to be fetched  |
| transfers   | array     | All parameters listed [here](https://razorpay.com/docs/api/route/#hold-settlements-for-transfers) are supported |

**Response:**
```json
{
  "entity": "collection",
  "count": 1,
  "items": [
    {
      "id": "trf_Jfm1KCF6w1oWgy",
      "entity": "transfer",
      "status": "pending",
      "source": "pay_JXPULbHbkkkS8D",
      "recipient": "acc_I0QRP7PpvaHhpB",
      "amount": 100,
      "currency": "INR",
      "amount_reversed": 0,
      "notes": [],
      "linked_account_notes": [],
      "on_hold": true,
      "on_hold_until": null,
      "recipient_settlement_id": null,
      "created_at": 1654860101,
      "processed_at": null,
      "error": {
        "code": null,
        "description": null,
        "reason": null,
        "field": null,
        "step": null,
        "id": "trf_Jfm1KCF6w1oWgy",
        "source": null,
        "metadata": null
      }
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Modify settlement hold for transfers
```py
client.transfer.edit(transferId,{
  "on_hold": True,
  "on_hold_until": "1679691505"
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| transferId*   | string      | The id of the payment to be fetched  |
| on_hold*   | boolean      | Possible values is `True` or `False`  |
| on_hold_until   | integer      | Timestamp, in Unix, that indicates until when the settlement of the transfer must be put on hold |

**Response:**
```json
{
    "entity": "collection",
    "count": 1,
    "items": [
        {
            "id": "trf_JhemwjNekar9Za",
            "entity": "transfer",
            "status": "pending",
            "source": "pay_I7watngocuEY4P",
            "recipient": "acc_HjVXbtpSCIxENR",
            "amount": 100,
            "currency": "INR",
            "amount_reversed": 0,
            "notes": [],
            "linked_account_notes": [],
            "on_hold": true,
            "on_hold_until": null,
            "recipient_settlement_id": null,
            "created_at": 1655271313,
            "processed_at": null,
            "error": {
                "code": null,
                "description": null,
                "reason": null,
                "field": null,
                "step": null,
                "id": "trf_JhemwjNekar9Za",
                "source": null,
                "metadata": null
            }
        }
    ]
}
```

-------------------------------------------------------------------------------------------------------

**PN: * indicates mandatory fields**
<br>
<br>
**For reference click [here](https://razorpay.com/docs/api/route/#transfers/)**