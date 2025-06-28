### Iin

### Token IIN API

```py
tokenIin = "412345"

client.iin.fetch(tokenIin)
```

**Parameters:**

| Name       | Type   | Description                       |
|------------|--------|-----------------------------------|
| tokenIin* | string | The token IIN. |

**Response:**
```json
{
  "iin": "412345",
  "entity": "iin",
  "network": "Visa",
  "type": "credit",
  "sub_type": "business",
  "issuer_code": "HDFC",
  "issuer_name": "HDFC Bank Ltd",
  "international": false,
  "is_tokenized": true,
  "card_iin": "411111",
  "emi":{
     "available": true
     },
  "recurring": {
     "available": true
     },
  "authentication_types": [
   {
       "type":"3ds"
   },
   {
       "type":"otp"
   }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Fetch All IINs Supporting Native OTP

```py
client.iin.all({"flow":"otp"})
```

**Parameters:**

| Name       | Type   | Description                       |
|------------|--------|-----------------------------------|
| flow | string | Authentication flow is Native OTP. Possible value is `otp`. |

**Response:**
```json
{
  "count": 24,
  "iins": [
    "512967",
    "180005",
    "401704",
    "401806",
    "123456",
    "411111",
    "123512967",
    "180012305",
    "401123704"
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Fetch All IINs with Business Sub-type

```py
client.iin.all({"sub_type":"business"})
```

**Parameters:**

| Name       | Type   | Description                       |
|------------|--------|-----------------------------------|
| sub_type | string | The sub_type of the IIN. Possible value is `business`. |

**Response:**
```json
{
  "count": 24,
  "iins": [
    "512967",
    "180005",
    "401704",
    "401806",
    "607389",
    "652203",
    "414367",
    "787878",
    "123456",
    "411111",
    "123512967",
    "180012305",
    "401123704"
  ]
}
```
-------------------------------------------------------------------------------------------------------

**PN: * indicates mandatory fields**
<br>
<br>
**For reference click [here](https://razorpay.com/docs/api/payments/cards/iin-api/#iin-entity)**