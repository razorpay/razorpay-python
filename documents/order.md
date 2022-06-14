## Orders

### Create order

```py
client.order.create({
  "amount": 50000,
  "currency": "INR",
  "receipt": "receipt#1",
  "notes": {
    "key1": "value3",
    "key2": "value2"
  }
})
```

**Parameters:**

| Name            | Type    | Description                                                                  |
|-----------------|---------|------------------------------------------------------------------------------|
| amount*          | integer | Amount of the order to be paid                                               |
| currency*        | string  | Currency of the order. Currently only `INR` is supported.                      |
| receipt         | string  | Your system order reference id.                                              |
| notes           | object  | A key-value pair   |
|partial_payment | boolean  | Indicates whether customers can make partial payments on the invoice . Possible values: true - Customer can make partial payments. false (default) - Customer cannot make partial payments. |

**Response:**

```json
{
  "id": "order_EKwxwAgItmmXdp",
  "entity": "order",
  "amount": 50000,
  "amount_paid": 0,
  "amount_due": 50000,
  "currency": "INR",
  "receipt": "receipt#1",
  "offer_id": null,
  "status": "created",
  "attempts": 0,
  "notes": [],
  "created_at": 1582628071
}
```

-------------------------------------------------------------------------------------------------------

### Fetch all orders

```py
client.order.all(option)
```

**Parameters**

| Name       | Type      | Description                                                  |
|------------|-----------|--------------------------------------------------------------|
| from       | timestamp | timestamp after which the orders were created              |
| to         | timestamp | timestamp before which the orders were created             |
| count      | integer   | number of orders to fetch (default: 10)                    |
| skip       | integer   | number of orders to be skipped (default: 0)                |
| authorized | boolean   | Orders for which orders are currently in authorized state. |
| receipt    | string    | Orders with the provided value for receipt.                  |
| expand[]   | string    |  Used to retrieve additional information about the payment. Possible value is `payments`,`payments.card`,`transfers` or `virtual_account` |
| authorized       | boolean | Possible value is `0` or `1` |


**Response:**

```json
{
  "entity": "collection",
  "count": 1,
  "items": [
    {
      "id": "order_EKzX2WiEWbMxmx",
      "entity": "order",
      "amount": 1234,
      "amount_paid": 0,
      "amount_due": 1234,
      "currency": "INR",
      "receipt": "Receipt No. 1",
      "offer_id": null,
      "status": "created",
      "attempts": 0,
      "notes": [],
      "created_at": 1582637108
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Fetch particular order

```py
client.order.fetch(orderId)
```
**Parameters**

| Name     | Type   | Description                         |
|----------|--------|-------------------------------------|
| orderId* | string | The id of the order to be fetched |

**Response:**

```json
{
  "id": "order_Jc81IZnaXSMLFh",
  "entity": "order",
  "amount": 50000,
  "amount_paid": 50000,
  "amount_due": 0,
  "currency": "INR",
  "receipt": null,
  "offer_id": null,
  "status": "paid",
  "attempts": 1,
  "notes": {
    "notes_key_1": "value1",
    "notes_key_2": "value2"
  },
  "created_at": 1654064215
}
```
-------------------------------------------------------------------------------------------------------

### Fetch payments for an order

```py
client.order.payments(orderId)
```
**Parameters**

| Name     | Type   | Description                         |
|----------|--------|-------------------------------------|
| orderId* | string | The id of the order to be retrieve payment info |

**Response:**
```json
{
  "entity": "collection",
  "count": 1,
  "items": [
    {
      "id": "pay_Jc81alhu5LmAUI",
      "entity": "payment",
      "amount": 50000,
      "currency": "INR",
      "status": "captured",
      "order_id": "order_Jc81IZnaXSMLFh",
      "invoice_id": "inv_Jc81IWvxf4TT1F",
      "international": false,
      "method": "upi",
      "amount_refunded": 0,
      "refund_status": null,
      "captured": true,
      "description": "Order # 2",
      "card_id": null,
      "bank": null,
      "wallet": null,
      "vpa": "success@razorpay",
      "email": "sofiya.shaikh2@razorpay.com",
      "contact": "+919702219003",
      "customer_id": "cust_JR4BVKjKyJ7enk",
      "token_id": "token_Jc81b6OBfodoi6",
      "notes": {
        "opencart_order_id": "2"
      },
      "fee": 1180,
      "tax": 180,
      "error_code": null,
      "error_description": null,
      "error_source": null,
      "error_step": null,
      "error_reason": null,
      "acquirer_data": {
        "rrn": "001000100002",
        "upi_transaction_id": "npci_txn_id_for_Jc81alhu5LmAUI"
      },
      "created_at": 1654064232
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Update order

```py
client.order.edit(orderId,{
  "notes": {
    "key1": "value3",
    "key2": "value2"
  }
})
```
**Parameters**

| Name     | Type   | Description                         |
|----------|--------|-------------------------------------|
| orderId* | string | The id of the order to be retrieve payment info |
| notes*   | object  | A key-value pair                    |

**Response:**
```json
{
  "id":"order_DaaS6LOUAASb7Y",
  "entity":"order",
  "amount":2200,
  "amount_paid":0,
  "amount_due":2200,
  "currency":"INR",
  "receipt":"Receipt #211",
  "offer_id":null,
  "status":"attempted",
  "attempts":1,
  "notes":{
    "notes_key_1":"Tea, Earl Grey, Hot",
    "notes_key_2":"Tea, Earl Grey… decaf."
  },
  "created_at":1572505143
}
```
-------------------------------------------------------------------------------------------------------


**PN: * indicates mandatory fields**
<br>
<br>
**For reference click [here](https://razorpay.com/docs/api/orders/)**