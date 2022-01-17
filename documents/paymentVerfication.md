## payment verification


### Verify payment verification

```py
client.utility.verify_payment_signature({
   'razorpay_order_id': razorpay_order_id,
   'razorpay_payment_id': razorpay_payment_id,
   'razorpay_signature': razorpay_signature
   })
```

**Parameters:**


| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| razorpay_order_id*  | string | The id of the order to be fetched  |
| razorpay_payment_id*    | string | The id of the payment to be fetched |
| razorpay_signature* | string   | Signature returned by the Checkout. This is used to verify the payment. |

-------------------------------------------------------------------------------------------------------
### Verify subscription verification

```py
client.utility.verify_subscription_payment_signature({
   'razorpay_subscription_id': razorpay_order_id,
   'razorpay_payment_id': razorpay_payment_id,
   'razorpay_signature': razorpay_signature
   })
```

**Parameters:**


| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| razorpay_subscription_id*  | string | The id of the subscription to be fetched  |
| razorpay_payment_id*    | string | The id of the payment to be fetched |
| razorpay_signature* | string   | Signature returned by the Checkout. This is used to verify the payment. |

-------------------------------------------------------------------------------------------------------
### Verify paymentlink verification

```py
client.utility.verify_payment_link_signature({
   'payment_link_id': payment_link_id,
   'payment_link_reference_id': payment_link_reference_id,
   'payment_link_status':payment_link_status,
   'razorpay_payment_id': razorpay_payment_id,
   'razorpay_signature': razorpay_signature
   })
```

**Parameters:**


| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| payment_link_id*  | string | The id of the paymentlink to be fetched  |
| razorpay_payment_id*  | string | The id of the payment to be fetched  |
| payment_link_reference_id*  | string |  A reference number tagged to a Payment Link |
| payment_link_status*  | string | Current status of the link  |
| razorpay_signature* | string   | Signature returned by the Checkout. This is used to verify the payment. |

-------------------------------------------------------------------------------------------------------

**PN: * indicates mandatory fields**
<br>
<br>