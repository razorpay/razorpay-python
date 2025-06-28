## Settlements

### Fetch all  settlements

```py
client.settlement.all(options)
```

**Parameters:**


| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| from  | timestamp | timestamp after which the settlement were created  |
| to    | timestamp | timestamp before which the settlement were created |
| count | integer   | number of settlements to fetch (default: 10)        |
| skip  | integer   | number of settlements to be skipped (default: 0)    |

**Response:**
```json
{
  "entity": "collection",
  "count": 1,
  "items": [
    {
      "id": "setl_DGlQ1Rj8os78Ec",
      "entity": "settlement",
      "amount": 9973635,
      "status": "processed",
      "fees": 471699,
      "tax": 42070,
      "utr": "1568176960vxp0rj",
      "created_at": 1568176960
    }
  ]
}
```

-------------------------------------------------------------------------------------------------------

### Fetch a settlement

```py
client.settlement.fetch(settlementId)
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| settlementId* | string      | The id of the settlement to be fetched  |

**Response:**
```json
{
    "id": "setl_DGlQ1Rj8os78Ec",
    "entity": "settlement",
    "amount": 9973635,
    "status": "processed",
    "fees": 471699,
    "tax": 42070,
    "utr": "1568176960vxp0rj",
    "created_at": 1568176960
}
```
-------------------------------------------------------------------------------------------------------

### Settlement recon

```py
client.settlement.report({
  "year": 2020,
  "month": 9,
  "day":11
})
```
**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| year* | integer      | The year the settlement was received in the `YYYY` format. For example, `2020`   |
| month* | integer      | The month the settlement was received in the `MM` format. For example, `09`   |
| day | integer   | The day the settlement was received in the `DD` format. For example,      |
| count | integer   | Specifies the number of available settlements to be fetched.    |
| skip | integer   | Specifies the number of available settlements to be skipped when fetching a count.  |

**Response:**
```json
{
  "entity": "collection",
  "count": 4,
  "items": [
    {
      "entity_id": "pay_DEXrnipqTmWVGE",
      "type": "payment",
      "debit": 0,
      "credit": 97100,
      "amount": 100000,
      "currency": "INR",
      "fee": 2900,
      "tax": 0,
      "on_hold": false,
      "settled": true,
      "created_at": 1567692556,
      "settled_at": 1568176960,
      "settlement_id": "setl_DGlQ1Rj8os78Ec",
      "posted_at": null,
      "credit_type": "default",
      "description": "Recurring Payment via Subscription",
      "notes": "{}",
      "payment_id": null,
      "settlement_utr": "1568176960vxp0rj",
      "order_id": "order_DEXrnRiR3SNDHA",
      "order_receipt": null,
      "method": "card",
      "card_network": "MasterCard",
      "card_issuer": "KARB",
      "card_type": "credit",
      "dispute_id": null
    },
    {
      "entity_id": "rfnd_DGRcGzZSLyEdg1",
      "type": "refund",
      "debit": 242500,
      "credit": 0,
      "amount": 242500,
      "currency": "INR",
      "fee": 0,
      "tax": 0,
      "on_hold": false,
      "settled": true,
      "created_at": 1568107224,
      "settled_at": 1568176960,
      "settlement_id": "setl_DGlQ1Rj8os78Ec",
      "posted_at": null,
      "credit_type": "default",
      "description": null,
      "notes": "{}",
      "payment_id": "pay_DEXq1pACSqFxtS",
      "settlement_utr": "1568176960vxp0rj",
      "order_id": "order_DEXpmZgffXNvuI",
      "order_receipt": null,
      "method": "card",
      "card_network": "MasterCard",
      "card_issuer": "KARB",
      "card_type": "credit",
      "dispute_id": null
    },
    {
      "entity_id": "trf_DEUoCEtdsJgvl7",
      "type": "transfer",
      "debit": 100296,
      "credit": 0,
      "amount": 100000,
      "currency": "INR",
      "fee": 296,
      "tax": 46,
      "on_hold": false,
      "settled": true,
      "created_at": 1567681786,
      "settled_at": 1568176960,
      "settlement_id": "setl_DGlQ1Rj8os78Ec",
      "posted_at": null,
      "credit_type": "default",
      "description": null,
      "notes": null,
      "payment_id": "pay_DEApNNTR6xmqJy",
      "settlement_utr": "1568176960vxp0rj",
      "order_id": null,
      "order_receipt": null,
      "method": null,
      "card_network": null,
      "card_issuer": null,
      "card_type": null,
      "dispute_id": null
    },
    {
      "entity_id": "adj_EhcHONhX4ChgNC",
      "type": "adjustment",
      "debit": 0,
      "credit": 1012,
      "amount": 1012,
      "currency": "INR",
      "fee": 0,
      "tax": 0,
      "on_hold": false,
      "settled": true,
      "created_at": 1567681786,
      "settled_at": 1568176960,
      "settlement_id": "setl_DGlQ1Rj8os78Ec",
      "posted_at": null,
      "description": "test reason",
      "notes": null,
      "payment_id": null,
      "settlement_utr": null,
      "order_id": null,
      "order_receipt": null,
      "method": null,
      "card_network": null,
      "card_issuer": null,
      "card_type": null,
      "dispute_id": null
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Create on-demand settlement

```py
client.settlement.create_ondemand_settlement({
  "amount": 1221,
  "settle_full_balance": false,
  "description": "Testing",
  "notes": {
    "notes_key_1": "Tea, Earl Grey, Hot",
    "notes_key_2": "Tea, Earl Grey… decaf."
  }
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| amount*| integer      | Maximum amount that can be settled  |
| settle_full_balance* | boolean      | true or false   |
| description | string   | The description may not be greater than 30 characters    |
| notes   | object   | A key-value pair     |

**Response:**
```json
{
  "id": "setlod_FNj7g2YS5J67Rz",
  "entity": "settlement.ondemand",
  "amount_requested": 200000,
  "amount_settled": 0,
  "amount_pending": 199410,
  "amount_reversed": 0,
  "fees": 590,
  "tax": 90,
  "currency": "INR",
  "settle_full_balance": false,
  "status": "initiated",
  "description": "Need this to make vendor payments.",
  "notes": {
    "notes_key_1": "Tea, Earl Grey, Hot",
    "notes_key_2": "Tea, Earl Grey… decaf."
  },
  "created_at": 1596771429,
  "ondemand_payouts": {
    "entity": "collection",
    "count": 1,
    "items": [
      {
        "id": "setlodp_FNj7g2cbvw8ueO",
        "entity": "settlement.ondemand_payout",
        "initiated_at": null,
        "processed_at": null,
        "reversed_at": null,
        "amount": 200000,
        "amount_settled": null,
        "fees": 590,
        "tax": 90,
        "utr": null,
        "status": "created",
        "created_at": 1596771429
      }
    ]
  }
}
```

Create on-demand settlement please click [here](https://razorpay.com/docs/api/settlements/instant/#create-an-instant-settlement)

-------------------------------------------------------------------------------------------------------

### Fetch all on-demand settlements

```py
client.settlement.fetch_all_ondemand_settlement(options)
```
**Parameters:**

| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| from  | timestamp | timestamp after which the settlements were created  |
| to    | timestamp | timestamp before which the settlements were created |
| count | integer   | number of settlements to fetch (default: 10)        |
| skip  | integer   | number of settlements to be skipped (default: 0)    |

**Response:**<br>

```json
{
  "entity": "collection",
  "count": 2,
  "items": [
    {
      "id": "setlod_FNj7g2YS5J67Rz",
      "entity": "settlement.ondemand",
      "amount_requested": 200000,
      "amount_settled": 199410,
      "amount_pending": 0,
      "amount_reversed": 0,
      "fees": 590,
      "tax": 90,
      "currency": "INR",
      "settle_full_balance": false,
      "status": "processed",
      "description": "Need this to make vendor payments.",
      "notes": {
        "notes_key_1": "Tea, Earl Grey, Hot",
        "notes_key_2": "Tea, Earl Grey… decaf."
      },
      "created_at": 1596771429
    },
    {
      "id": "setlod_FJOp0jOWlalIvt",
      "entity": "settlement.ondemand",
      "amount_requested": 300000,
      "amount_settled": 299114,
      "amount_pending": 0,
      "amount_reversed": 0,
      "fees": 886,
      "tax": 136,
      "currency": "INR",
      "settle_full_balance": false,
      "status": "processed",
      "description": "Need this to buy stock.",
      "notes": {
        "notes_key_1": "Tea, Earl Grey, Hot",
        "notes_key_2": "Tea, Earl Grey… decaf."
      },
      "created_at": 1595826576
    }
  ]
}
```

-------------------------------------------------------------------------------------------------------

### Fetch on-demand settlement by ID

```py
client.settlement.fetch_ondemand_settlement_id(settlementId)
```

**Parameters:**

| Name       | Type   | Description                       |
|------------|--------|-----------------------------------|
| settlementId* | string | Settlement Id of the On-demand settlement|

**Response:**

```json
{
  "id": "setlod_FNj7g2YS5J67Rz",
  "entity": "settlement.ondemand",
  "amount_requested": 200000,
  "amount_settled": 199410,
  "amount_pending": 0,
  "amount_reversed": 0,
  "fees": 590,
  "tax": 90,
  "currency": "INR",
  "settle_full_balance": false,
  "status": "processed",
  "description": "Need this to make vendor payments.",
  "notes": {
    "notes_key_1": "Tea, Earl Grey, Hot",
    "notes_key_2": "Tea, Earl Grey… decaf."
  },
  "created_at": 1596771429
}
```
-------------------------------------------------------------------------------------------------------

**PN: * indicates mandatory fields**
<br>
<br>
**For reference click [here](https://razorpay.com/docs/api/settlements/)**