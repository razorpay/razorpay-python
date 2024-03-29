# Razorpay Python Client

[![PyPI Version](https://img.shields.io/pypi/v/razorpay.svg)](https://pypi.python.org/pypi/razorpay) [![Coverage Status](https://coveralls.io/repos/github/razorpay/razorpay-python/badge.svg?branch=master)](https://coveralls.io/github/razorpay/razorpay-python?branch=master) [![PyPI](https://img.shields.io/badge/python-3%20%7C%203.4%20%7C%203.5%20%7C%203.6-blue.svg)]() [![License](https://img.shields.io/:license-mit-blue.svg)](https://opensource.org/licenses/MIT)

Python bindings for interacting with the Razorpay API

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

## App Details

After setting up client, you can set your app details before making any request
to Razorpay using the following:

```py
client.set_app_details({"title" : "<YOUR_APP_TITLE>", "version" : "<YOUR_APP_VERSION>"})
```

For example, you can set the title to `Django` and version to `1.8.17`. Please ensure
that both app title and version are strings.

## Supported Resources
- [Account](documents/account.md)

- [Addon](documents/addon.md)

- [Item](documents/items.md)

- [Customer](documents/customer.md)

- [Token](documents/token.md)

- [Fund](documents/fund.md)

- [Order](documents/order.md)

- [Payments](documents/payment.md)

- [Settlements](documents/settlement.md)

- [Refunds](documents/refund.md)

- [Invoice](documents/invoice.md)

- [Subscriptions](documents/subscription.md)

- [Payment Links](documents/paymentLink.md)

- [Smart Collect](documents/virtualAccount.md)

- [Route](documents/transfer.md)

- [QR Code](documents/qrcode.md)

- [Emandate](documents/emandate.md)

- [Cards](documents/card.md)

- [Paper NACH](documents/papernach.md)

- [UPI](documents/upi.md)

- [Register Emandate and Charge First Payment Together](documents/registerEmandate.md)

- [Register NACH and Charge First Payment Together](documents/registerNach.md)

- [Payment Verification](documents/paymentVerfication.md)

- [Product Configuration](documents/productConfiguration.md)

- [Stakeholder](documents/stakeholder.md)

- [Webhook](documents/webhook.md)

- [Document](documents/document.md)

- [Dispute](documents/dispute.md)

- [Iin](documents/iin.md)
---

## Bugs? Feature requests? Pull requests?

All of those are welcome. You can [file issues][issues] or [submit pull requests][pulls] in this repository.

[issues]: https://github.com/razorpay/razorpay-python/issues
[pulls]: https://github.com/razorpay/razorpay-python/pulls
