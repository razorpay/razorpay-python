## items

### Create item

```py
client.item.create({
  "name": "Book / English August",
  "description": "An indian story, Booker prize winner.",
  "amount": 20000,
  "currency": "INR"
})
```

**Parameters:**

| Name            | Type    | Description                                                                  |
|-----------------|---------|------------------------------------------------------------------------------|
| name*          | string | Name of the item.                    |
| description        | string  | A brief description of the item.  |
| amount*         | integer  | Amount of the order to be paid     |
| currency*           | string  | Currency of the order. Currently only `INR` is supported.    |

**Response:**
```json
{
  "id": "item_JnQ2kRGq8Kbte3",
  "active": true,
  "name": "Book / English August",
  "description": "An indian story, Booker prize winner.",
  "amount": 20000,
  "unit_amount": 20000,
  "currency": "INR",
  "type": "invoice",
  "unit": null,
  "tax_inclusive": false,
  "hsn_code": null,
  "sac_code": null,
  "tax_rate": null,
  "tax_id": null,
  "tax_group_id": null,
  "created_at": 1656529427
}
```

-------------------------------------------------------------------------------------------------------

### Fetch all items

```py
client.item.all(options)
```
**Parameters:**

| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| from  | timestamp | timestamp after which the item were created  |
| to    | timestamp | timestamp before which the item were created |
| count | integer   | number of item to fetch (default: 10)        |
| skip  | integer   | number of item to be skipped (default: 0)    |
| active  | integer   | Fetches number of active or inactive items. The value is `1` for active items and `0` for inactive items. |

**Response:**
```json
{
  "entity": "collection",
  "count": 1,
  "items": [
    {
      "id": "item_JnQ2kRGq8Kbte3",
      "active": true,
      "name": "Book / English August",
      "description": "An indian story, Booker prize winner.",
      "amount": 20000,
      "unit_amount": 20000,
      "currency": "INR",
      "type": "invoice",
      "unit": null,
      "tax_inclusive": false,
      "hsn_code": null,
      "sac_code": null,
      "tax_rate": null,
      "tax_id": null,
      "tax_group_id": null,
      "created_at": 1656529427
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------
### Fetch particular item

```py
client.item.fetch(itemId)
```
**Parameters**

| Name     | Type   | Description                         |
|----------|--------|-------------------------------------|
| itemId* | string | The id of the item to be fetched |

**Response:**
```json
{
  "id": "item_JnQ2kRGq8Kbte3",
  "active": true,
  "name": "Book / English August",
  "description": "An indian story, Booker prize winner.",
  "amount": 20000,
  "unit_amount": 20000,
  "currency": "INR",
  "type": "invoice",
  "unit": null,
  "tax_inclusive": false,
  "hsn_code": null,
  "sac_code": null,
  "tax_rate": null,
  "tax_id": null,
  "tax_group_id": null,
  "created_at": 1656529427
}
```

-------------------------------------------------------------------------------------------------------

### Update item

```py
client.item.edit(itemId,{
  "name": "Book / Ignited Minds - Updated name!",
  "description": "New descirption too. :).",
  "amount": 20000,
  "currency": "INR",
  "active": True
})
```
**Parameters**

| Name     | Type   | Description                         |
|----------|--------|-------------------------------------|
| itemId* | string | The id of the item to be fetched |
| name       | string | Name of the item.                    |
| description  | string  | A brief description of the item.  |
| amount         | integer  | Amount of the order to be paid     |
| currency           | string  | Currency of the order. Currently only `INR` is supported.    |
| active   | boolean  | Possible values is `0` or `1` |

**Response:**
```json
{
  "id": "item_JnQ2kRGq8Kbte3",
  "active": true,
  "name": "Book / Ignited Minds - Updated name!",
  "description": "New descirption too. :).",
  "amount": 20000,
  "unit_amount": 20000,
  "currency": "INR",
  "type": "invoice",
  "unit": null,
  "tax_inclusive": false,
  "hsn_code": null,
  "sac_code": null,
  "tax_rate": null,
  "tax_id": null,
  "tax_group_id": null,
  "created_at": 1656529427
}
```
-------------------------------------------------------------------------------------------------------
### Delete item

```py
client.item.delete(itemId)
```
**Parameters**

| Name     | Type   | Description                         |
|----------|--------|-------------------------------------|
| itemId* | string | The id of the item to be fetched |

**Response:**
```json
[]
```
-------------------------------------------------------------------------------------------------------

**PN: * indicates mandatory fields**
<br>
<br>
**For reference click [here](https://razorpay.com/docs/api/items)**