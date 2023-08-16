## Orders

### Create order

```py
client.order.create({
  "amount": 50000,
  "currency": "INR",
  "receipt": "receipt#1",
  "partial_payment":False,
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

### Create order (Third party validation)

```py
client.order.create({
  "amount": 500,
  "method": "netbanking",
  "receipt": "BILL13375649",
  "currency": "INR",
  "bank_account": {
    "account_number": "765432123456789",
    "name": "Gaurav Kumar",
    "ifsc": "HDFC0000053"
  }
})
```

**Parameters:**

| Name            | Type    | Description                                                                  |
|-----------------|---------|------------------------------------------------------------------------------|
| amount*          | integer | Amount of the order to be paid                                               |
| method        | string  | The payment method used to make the payment. If this parameter is not passed, customers will be able to make payments using both netbanking and UPI payment methods. Possible values is `netbanking` or `upi`|
| currency*        | string  | Currency of the order. Currently only `INR` is supported.       |
| receipt         | string  | Your system order reference id.                                              |
| notes         | array      | A key-value pair  |
|bank_account | array  | All keys listed [here](https://razorpay.com/docs/payments/third-party-validation/#step-2-create-an-order) are supported |

**Response:**

```json
{
  "id": "order_GAWN9beXgaqRyO",
  "entity": "order",
  "amount": 500,
  "amount_paid": 0,
  "amount_due": 500,
  "currency": "INR",
  "receipt": "BILL13375649",
  "offer_id": null,
  "status": "created",
  "attempts": 0,
  "notes": [],
  "created_at": 1573044247
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
      "email": "gaurav.kumar@example.com",
      "contact": "+919999999999",
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