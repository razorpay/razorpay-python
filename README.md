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
razor = razorpay.Client(auth=("<YOUR_API_KEY>", "<YOUR_API_SECRET>"))
```


### Payments

- Capture a payment

    ```py
    razor.payment.capture("<PAYMENT_ID>", "<AMOUNT>")
    ```

- Fetch a particular payment

    ```py
    razor.payment.fetch("<PAYMENT_ID>")
    ```

- Fetch all payments

    ```py
    razor.payment.all()
    ```

### Refunds

- Initiate a refund

    ```py
    razor.refund.create("<PAYMENT_ID>")  # for whole amount
    razor.refund.create("<PAYMENT_ID>", data={"amount": "<AMOUNT_TO_BE_REFUNDED>"})  # for particular amount
    ```

- Fetch a particular refund

    ```py
    razor.refund.fetch("<PAYMENT_ID>", "<REFUND_ID>")
    ```

- Fetch all refunds for a particular payment

    ```py
    razor.refund.all("<PAYMENT_ID>")
    ```

## Bugs? Feature requests? Pull requests?

All of those are welcome. You can [file issues][issues] or [submit pull requests][pulls] in this repository.

[issues]: https://github.com/decached/razorpay/issues
[pulls]: https://github.com/decached/razorpay/pulls
