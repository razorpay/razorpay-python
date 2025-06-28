## Product Configuration 

### Request a Product Configuration
```py

accountId = "acc_GP4lfNA0iIMn5B"

client.product.requestProductConfiguration(accountId, {
    "product_name" : "payment_gateway",
    "tnc_accepted" : True,
    "ip" : "233.233.233.234"
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| product_name* | string   | The product(s) to be configured. Possible value is `payment_gateway`, `payment_links`  |
| tnc_accepted        | boolean      | Pass this parameter to accept terms and conditions. Send this parameter along with the ip parameter when the tnc is accepted. Possible values is `true`  |
| ip          | integer      | The IP address of the merchant while accepting the terms and conditions. Send this parameter along with the `tnc_accepted` parameter when the `tnc` is accepted.  |

**Response:**
```json
{
  "requested_configuration": {
    "payment_methods": []
  },
  "active_configuration": {
    "payment_capture": {
      "mode": "automatic",
      "refund_speed": "normal",
      "automatic_expiry_period": 7200
    },
    "settlements": {
      "account_number": null,
      "ifsc_code": null,
      "beneficiary_name": null
    },
    "checkout": {
      "theme_color": "#FFFFFF",
      "flash_checkout": true,
      "logo": "https://example.com/your_logo"
    },
    "refund": {
      "default_refund_speed": "normal"
    },
    "notifications": {
      "whatsapp": true,
      "sms": false,
      "email": [
        "b963e252-1201-45b0-9c39-c53eceb0cfd6_load@gmail.com"
      ]
    },
    "payment_methods": {
      "netbanking": {
        "enabled": true,
        "instrument": [
          {
            "type": "retail",
            "bank": [
              "hdfc",
              "sbin",
              "utib",
              "icic",
              "scbl",
              "yesb"
            ]
          }
        ]
      },
      "wallet": {
        "enabled": true,
        "instrument": [
          "airtelmoney",
          "freecharge",
          "jiomoney",
          "olamoney",
          "payzapp",
          "mobikwik"
        ]
      },
      "upi": {
        "enabled": true,
        "instrument": [
          "upi"
        ]
      }
    }
  },
  "requirements": [
    {
      "field_reference": "individual_proof_of_address",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/stakeholders/{stakeholderId}/documents",
      "status": "required",
      "reason_code": "document_missing"
    },
    {
      "field_reference": "individual_proof_of_identification",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/stakeholders/{stakeholderId}/documents",
      "status": "required",
      "reason_code": "document_missing"
    },
    {
      "field_reference": "business_proof_of_identification",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/documents",
      "status": "required",
      "reason_code": "document_missing"
    },
    {
      "field_reference": "settlements.beneficiary_name",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/products/acc_prd_HEgNpywUFctQ9e",
      "status": "required",
      "reason_code": "field_missing"
    },
    {
      "field_reference": "settlements.account_number",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/products/acc_prd_HEgNpywUFctQ9e",
      "status": "required",
      "reason_code": "field_missing"
    },
    {
      "field_reference": "settlements.ifsc_code",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/products/acc_prd_HEgNpywUFctQ9e",
      "status": "required",
      "reason_code": "field_missing"
    },
    {
      "field_reference": "contact_name",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0",
      "status": "required",
      "reason_code": "field_missing"
    },
    {
      "field_reference": "name",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/stakeholders",
      "status": "required",
      "reason_code": "field_missing"
    },
    {
      "field_reference": "customer_facing_business_name",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0",
      "status": "required",
      "reason_code": "field_missing"
    },
    {
      "field_reference": "kyc.pan",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/stakeholders",
      "status": "required",
      "reason_code": "field_missing"
    }
  ],
  "tnc":{
    "id": "tnc_IgohZaDBHRGjPv",
    "accepted": true,
    "accepted_at": 1641550798
  },
  "id": "acc_prd_HEgNpywUFctQ9e",
  "account_id": "acc_HQVlm3bnPmccC0",
  "product_name": "payment_gateway",
  "activation_status": "needs_clarification",
  "requested_at": 162547884
}
```

-------------------------------------------------------------------------------------------------------

### Edit a Product Configuration
```py
accountId = "acc_GP4lfNA0iIMn5B"
productId = "acc_prd_HEgNpywUFctQ9e"

client.product.edit(accountId, productId, {
  "notifications": {
    "email": [
      "gaurav.kumar@example.com",
      "acd@gmail.com"
    ]
  },
  "checkout": {
    "theme_color": "#528FFF"
  },
  "refund": {
    "default_refund_speed": "optimum"
  },
  "settlements": {
    "account_number": "1234567890",
    "ifsc_code": "HDFC0000317",
    "beneficiary_name": "Gaurav Kumar"
  },
  "tnc_accepted": True,
  "ip": "233.233.233.234"
})
```

**Parameters:**

| Name          | Type        | Description                                 |
|---------------|-------------|---------------------------------------------|
| notifications          | object      | All keys listed [here](https://razorpay.com/docs/api/partners/product-configuration/#update-a-product-configuration) are supported | 
| checkout      | object      | All keys listed [here](https://razorpay.com/docs/api/partners/product-configuration/#update-a-product-configuration) are supported | 
| refund | object      | All keys listed [here](https://razorpay.com/docs/api/partners/product-configuration/#update-a-product-configuration) are supported | 
| settlements         | object      | All keys listed [here](https://razorpay.com/docs/api/partners/product-configuration/#update-a-product-configuration) are supported |         
| tnc_accepted         | boolean      |  Pass this parameter to accept terms and conditions. Send this parameter along with the ip parameter when the tnc is accepted. Possible value is `true` |
| ip         | string      | The IP address of the merchant while accepting the terms and conditions. Send this parameter along with the tnc_accepted parameter when the `tnc` is accepted. |
| payment_methods | All keys listed [here](https://razorpay.com/docs/api/partners/product-configuration/#update-a-product-configuration) are supported | 
| type | string  | Possible value is `domestic` |
| issuer | string  | The card issuer. Possible values for issuer are `amex`, `dicl`, `maestro`, `mastercard`, `rupay`, `visa`. |     
| wallet | object  | All keys listed [here](https://razorpay.com/docs/api/partners/product-configuration/#update-a-product-configuration) are supported |   
| instrument(wallet) | string  | The wallet issuer. Possible values are `airtelmoney`, `amazonpay`, `freecharge`, `jiomoney`, `mobiwik`, `mpesa`, `olamoney`, `paytm`, `payzapp`, `payumoney`, `phonepe`, `phonepeswitch`, `sbibuddy` |  
| instrument(wallet) | string  | The wallet issuer. Possible values are `airtelmoney`, `amazonpay`, `freecharge`, `jiomoney`, `mobiwik`, `mpesa`, `olamoney`, `paytm`, `payzapp`, `payumoney`, `phonepe`, `phonepeswitch`, `sbibuddy` | 
| upi | object  | All keys listed [here](https://razorpay.com/docs/api/partners/product-configuration/#update-a-product-configuration) are supported |  
| instrument(upi) | string  | The UPI service provider. Possible values are `google_pay`, `upi`| 
| paylater | object  | All keys listed [here](https://razorpay.com/docs/api/partners/product-configuration/#update-a-product-configuration) are supported |  
| instrument(emi) | string  | The Paylater service provider. Possible values are `epaylater`, `getsimpl`| 
| emi | object  | All keys listed [here](https://razorpay.com/docs/api/partners/product-configuration/#update-a-product-configuration) are supported |        

**Response:**
```json
{
  "id": "acc_GP4lfNA0iIMn5B",
  "type": "standard",
  "status": "created",
  "email": "gauri@example.org",
  "profile": {
    "category": "healthcare",
    "subcategory": "clinic",
    "addresses": {
      "registered": {
        "street1": "507, Koramangala 1st block",
        "street2": "MG Road-1",
        "city": "Bengalore",
        "state": "KARNATAKA",
        "postal_code": "560034",
        "country": "IN"
      }
    }
  },
  "notes": [],
  "created_at": 1610603081,
  "phone": "9000090000",
  "reference_id": "randomId",
  "business_type": "partnership",
  "legal_business_name": "Acme Corp",
  "customer_facing_business_name": "ABCD Ltd"
}
```
-------------------------------------------------------------------------------------------------------

### Fetch a product configuration
```py
accountId = "acc_GP4lfNA0iIMn5B"

productId = "acc_prd_HEgNpywUFctQ9e"

client.product.fetch(accountId, productId)
```

**Parameters:**

| Name        | Type        | Description                                 |
|-------------|-------------|---------------------------------------------|
| accountId* | string      | The unique identifier of a sub-merchant account generated by Razorpay.  |
| productId* | string      | The unique identifier of a product generated by Razorpay.  |

**Response:**
```json
{
  "requested_configuration": {
    "payment_methods": []
  },
  "active_configuration": {
    "payment_capture": {
      "mode": "automatic",
      "refund_speed": "normal",
      "automatic_expiry_period": 7200
    },
    "settlements": {
      "account_number": null,
      "ifsc_code": null,
      "beneficiary_name": null
    },
    "checkout": {
      "theme_color": "#FFFFFF",
      "flash_checkout": true
    },
    "refund": {
      "default_refund_speed": "normal"
    },
    "notifications": {
      "whatsapp": true,
      "sms": false,
      "email": [
        "b963e252-1201-45b0-9c39-c53eceb0cfd6_load@gmail.com"
      ]
    },
    "payment_methods": {
      "netbanking": {
        "enabled": true,
        "instrument": [
          {
            "type": "retail",
            "bank": [
              "hdfc",
              "sbin",
              "utib",
              "icic",
              "scbl",
              "yesb"
            ]
          }
        ]
      },
      "wallet": {
        "enabled": true,
        "instrument": [
          "airtelmoney",
          "freecharge",
          "jiomoney",
          "olamoney",
          "payzapp",
          "mobikwik"
        ]
      },
      "upi": {
        "enabled": true,
        "instrument": [
          "upi"
        ]
      }
    }
  },
  "requirements": [
    {
      "field_reference": "individual_proof_of_address",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/stakeholders/{stakeholderId}/documents",
      "status": "required",
      "reason_code": "document_missing"
    },
    {
      "field_reference": "individual_proof_of_identification",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/stakeholders/{stakeholderId}/documents",
      "status": "required",
      "reason_code": "document_missing"
    },
    {
      "field_reference": "business_proof_of_identification",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/documents",
      "status": "required",
      "reason_code": "document_missing"
    },
    {
      "field_reference": "settlements.beneficiary_name",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/products/acc_prd_HEgNpywUFctQ9e",
      "status": "required",
      "reason_code": "field_missing"
    },
    {
      "field_reference": "settlements.account_number",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/products/acc_prd_HEgNpywUFctQ9e",
      "status": "required",
      "reason_code": "field_missing"
    },
    {
      "field_reference": "settlements.ifsc_code",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/products/acc_prd_HEgNpywUFctQ9e",
      "status": "required",
      "reason_code": "field_missing"
    },
    {
      "field_reference": "contact_name",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0",
      "status": "required",
      "reason_code": "field_missing"
    },
    {
      "field_reference": "name",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/stakeholders",
      "status": "required",
      "reason_code": "field_missing"
    },
    {
      "field_reference": "customer_facing_business_name",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0",
      "status": "required",
      "reason_code": "field_missing"
    },
    {
      "field_reference": "kyc.pan",
      "resolution_url": "/accounts/acc_HQVlm3bnPmccC0/stakeholders",
      "status": "required",
      "reason_code": "field_missing"
    }
  ],
  "tnc":{
    "id": "tnc_IgohZaDBHRGjPv",
    "accepted": true,
    "accepted_at": 1641550798
  },
  "id": "acc_prd_HEgNpywUFctQ9e",
  "account_id": "acc_HQVlm3bnPmccC0",
  "product_name": "payment_gateway",
  "activation_status": "needs_clarification",
  "requested_at": 1625478849
}
```

-------------------------------------------------------------------------------------------------------

### Fetch Terms and Conditions for a Sub-Merchant
```py

productName = "payments"

client.product.fetchTnc(productName)
```

**Parameters:**

| Name        | Type        | Description                                 |
|-------------|-------------|---------------------------------------------|
| productName* | string      | The product family for which the relevant product to be requested for the sub-merchant. Possible value is `payments`  |

**Response:**
```json
{
  "entity": "tnc_map",
  "product_name": "payments",
  "id": "tnc_map_HjOVhIdpVDZ0FB",
  "tnc": {
    "terms": "https://razorpay.com/terms",
    "privacy": "https://razorpay.com/privacy",
    "agreement": "https://razorpay.com/agreement"
  },
  "last_published_at": 1640589653
}
```

-------------------------------------------------------------------------------------------------------

**PN: * indicates mandatory fields**
<br>
<br>
**For reference click [here](https://razorpay.com/docs/api/partners/product-configuration/)**