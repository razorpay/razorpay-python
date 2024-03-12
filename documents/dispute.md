## Document

### Fetch All Disputes

```py
client.dispute.all()
```

**Response:**
```json
{
  "entity": "collection",
  "count": 1,
  "items": [
    {
      "id": "disp_Esz7KAitoYM7PJ",
      "entity": "dispute",
      "payment_id": "pay_EsyWjHrfzb59eR",
      "amount": 10000,
      "currency": "INR",
      "amount_deducted": 0,
      "reason_code": "pre_arbitration",
      "respond_by": 1590604200,
      "status": "open",
      "phase": "pre_arbitration",
      "created_at": 1590059211,
      "evidence": {
        "amount": 10000,
        "summary": null,
        "shipping_proof": null,
        "billing_proof": null,
        "cancellation_proof": null,
        "customer_communication": null,
        "proof_of_service": null,
        "explanation_letter": null,
        "refund_confirmation": null,
        "access_activity_log": null,
        "refund_cancellation_policy": null,
        "term_and_conditions": null,
        "others": null,
        "submitted_at": null
      }
    }
  ]
}
```
-------------------------------------------------------------------------------------------------------

### Fetch a Dispute

```py
disputeId = "disp_0000000000000";

client.dispute.fetch(disputeId);
```

**Parameters:**

| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| disputeId*  | string | The unique identifier of the dispute.  |

**Response:**
```json
{
  "id": "disp_AHfqOvkldwsbqt",
  "entity": "dispute",
  "payment_id": "pay_EsyWjHrfzb59eR",
  "amount": 10000,
  "currency": "INR",
  "amount_deducted": 0,
  "reason_code": "pre_arbitration",
  "respond_by": 1590604200,
  "status": "open",
  "phase": "pre_arbitration",
  "created_at": 1590059211,
  "evidence": {
    "amount": 10000,
    "summary": "goods delivered",
    "shipping_proof": null,
    "billing_proof": null,
    "cancellation_proof": null,
    "customer_communication": null,
    "proof_of_service": null,
    "explanation_letter": null,
    "refund_confirmation": null,
    "access_activity_log": null,
    "refund_cancellation_policy": null,
    "term_and_conditions": null,
    "others": null,
    "submitted_at": null
  }
}
```
-------------------------------------------------------------------------------------------------------

### Fetch a Dispute

```py
disputeId = "disp_0000000000000";

client.dispute.accept(disputeId);
```

**Parameters:**

| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| disputeId*  | string | The unique identifier of the dispute.  |

**Response:**
```json
{
  "id": "disp_AHfqOvkldwsbqt",
  "entity": "dispute",
  "payment_id": "pay_EsyWjHrfzb59eR",
  "amount": 10000,
  "currency": "INR",
  "amount_deducted": 10000,
  "reason_code": "pre_arbitration",
  "respond_by": 1590604200,
  "status": "lost",
  "phase": "pre_arbitration",
  "created_at": 1590059211,
  "evidence": {
    "amount": 10000,
    "summary": null,
    "shipping_proof": null,
    "billing_proof": null,
    "cancellation_proof": null,
    "customer_communication": null,
    "proof_of_service": null,
    "explanation_letter": null,
    "refund_confirmation": null,
    "access_activity_log": null,
    "refund_cancellation_policy": null,
    "term_and_conditions": null,
    "others": null,
    "submitted_at": null
  }
}
```
-------------------------------------------------------------------------------------------------------
### Contest a Dispute

```py
# Use this API sample code for draft

disputeId = "disp_0000000000000";

client.dispute.contest(disputeId,{
  "amount": 5000,
  "summary": "goods delivered",
  "shipping_proof": [
    "doc_EFtmUsbwpXwBH9",
    "doc_EFtmUsbwpXwBH8"
  ],
  "others": [
    {
      "type": "receipt_signed_by_customer",
      "document_ids": [
        "doc_EFtmUsbwpXwBH1",
        "doc_EFtmUsbwpXwBH7"
      ]
    }
  ],
  "action": "draft"
})
```

**Parameters:**

| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| disputeId*  | string | The unique identifier of the dispute.  |
| amount  | integer | The amount being contested. If the contest amount is not mentioned, we will assume it to be a full dispute contest.  |
| summary  | string | The explanation provided by you for contesting the dispute. It can have a maximum length of 1000 characters. |
| shipping_proof  | array | List of document ids which serves as proof that the product was shipped to the customer at their provided address. It should show their complete shipping address, if possible. |
| others  | array | All keys listed [here](https://razorpay.com/docs/api/disputes/contest) are supported |

```py
# Use this API sample code for submit

client.dispute.contest(disputeId,{
  "billing_proof": [
    "doc_EFtmUsbwpXwBG9",
    "doc_EFtmUsbwpXwBG8"
  ],
  "action": "submit"
})
```

**Response:**
```json
// Draft
{
  "id": "disp_AHfqOvkldwsbqt",
  "entity": "dispute",
  "payment_id": "pay_EsyWjHrfzb59eR",
  "amount": 10000,
  "currency": "INR",
  "amount_deducted": 0,
  "reason_code": "chargeback",
  "respond_by": 1590604200,
  "status": "open",
  "phase": "chargeback",
  "created_at": 1590059211,
  "evidence": {
    "amount": 5000,
    "summary": "goods delivered",
    "shipping_proof": [
      "doc_EFtmUsbwpXwBH9",
      "doc_EFtmUsbwpXwBH8"
    ],
    "billing_proof": null,
    "cancellation_proof": null,
    "customer_communication": null,
    "proof_of_service": null,
    "explanation_letter": null,
    "refund_confirmation": null,
    "access_activity_log": null,
    "refund_cancellation_policy": null,
    "term_and_conditions": null,
    "others": [
      {
        "type": "receipt_signed_by_customer",
        "document_ids": [
          "doc_EFtmUsbwpXwBH1",
          "doc_EFtmUsbwpXwBH7"
        ]
      }
    ],
    "submitted_at": null
  }
}

//Submit 
{
  "id": "disp_AHfqOvkldwsbqt",
  "entity": "dispute",
  "payment_id": "pay_EsyWjHrfzb59eR",
  "amount": 10000,
  "currency": "INR",
  "amount_deducted": 0,
  "reason_code": "chargeback",
  "respond_by": 1590604200,
  "status": "under_review",
  "phase": "chargeback",
  "created_at": 1590059211,
  "evidence": {
    "amount": 5000,
    "summary": "goods delivered",
    "shipping_proof": [
      "doc_EFtmUsbwpXwBH9",
      "doc_EFtmUsbwpXwBH8"
    ],
    "billing_proof": [
      "doc_EFtmUsbwpXwBG9",
      "doc_EFtmUsbwpXwBG8"
    ],
    "cancellation_proof": null,
    "customer_communication": null,
    "proof_of_service": null,
    "explanation_letter": null,
    "refund_confirmation": null,
    "access_activity_log": null,
    "refund_cancellation_policy": null,
    "term_and_conditions": null,
    "others": [
      {
        "type": "receipt_signed_by_customer",
        "document_ids": [
          "doc_EFtmUsbwpXwBH1",
          "doc_EFtmUsbwpXwBH7"
        ]
      }
    ],
    "submitted_at": 1590603200
  }
}
```
-------------------------------------------------------------------------------------------------------
**PN: * indicates mandatory fields**
<br>
<br>
**For reference click [here](https://razorpay.com/docs/api/documents)**