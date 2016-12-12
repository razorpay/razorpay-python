# Razorpay Python Client

[![PyPI Version](https://img.shields.io/pypi/v/razorpay.svg?style=flat-square)](https://pypi.python.org/pypi/razorpay) [![Build Status](https://travis-ci.org/razorpay/razorpay-python.svg?branch=master)](https://travis-ci.org/razorpay/razorpay-python) [![License](https://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Python bindings for interacting with the Razorpay API. 

This is primarily meant for merchants who wish to perform interactions with the Razorpay API programatically.

## Installation

```sh
$ pip install razorpay
```

## Usage

You need to setup your key and secret using the following:
You can find your API keys at <https://dashboard.razorpay.com/#/app/keys>.

```py
import razorpay
client = razorpay.Client(auth=("<YOUR_API_KEY>", "<YOUR_API_SECRET>"))
```

### Payments

- Fetch all payments

    ```py
    client.payment.fetch_all()
    ```

- Fetch a particular payment

    ```py
    client.payment.fetch("<PAYMENT_ID>")
    ```

- Capture a payment

    ```py
    client.payment.capture("<PAYMENT_ID>", "<AMOUNT>")
    Note: <AMOUNT> should be same as the original amount while creating the payment
    ```

- Refund a payment

    ```py
    client.payment.refund("<PAYMENT_ID>", "<AMOUNT>") 
    # for full refund

    client.payment.refund("<PAYMENT_ID>", "<AMOUNT_TO_BE_REFUNDED>") 
    # for particular amount

    Note: <AMOUNT_TO_BE_REFUNDED> should be equal/less than the original amount
    ```

### Refunds

- fetch a particular refund

    ```py
    client.refund.fetch("<payment_id>", "<refund_id>")
    ```

- fetch all refunds for a particular payment(same as payment refund fetch all)
   
    ```py
    client.refund.fetch_all("<payment_id>")
    ```

### Orders

- Create a new order

    ```py
    client.order.create(data=DATA)
    DATA should contain these keys
        amount           : amount of order
        currency         : currency of order
        receipt          : receipt id of order
        payment_capture  : 1 if capture should be done automatically or else 0
        notes(optional)  : optional notes for order
    ```

- fetch a particular order

    ```py
    client.order.fetch("<ORDER_ID>")
    ```

- fetch all orders 
   
    ```py
    client.order.fetch_all()
    ```

- fetch Payments of order 
   
    ```py
    client.order.fetch_all_payments("<ORDER_ID>")
    ```

### Invoices

- Create a new invoice

    ```py
    client.invoice.create(data=DATA)
    ```
    For List of params refer to this :-
    https://docs.razorpay.com/v1/page/invoices#v1invoices


- fetch a particular invoice

    ```py
    client.invoice.fetch("<INVOICE_ID>")
    ```

- fetch all invoices
   
    ```py
    client.invoice.fetch_all()
    ```

## Bugs? Feature requests? Pull requests?

All of those are welcome. You can [file issues][issues] or [submit pull requests][pulls] in this repository.

[issues]: https://github.com/razorpay/razorpay-python/issues
[pulls]: https://github.com/razorpay/razorpay-python/pulls
