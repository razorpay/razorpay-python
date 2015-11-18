# Razorpay Python Client

[![License](https://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://decached.mit-license.org)

Python bindings for interacting with the Razorpay API. 

This is primarily meant for merchants who wish to perform interactions with the
Razorpay API programatically.

## Installation

```sh
$ pip install razorpay
```

## Usage

You need to setup your key and secret using the following:

```py
import razorpay
razor = razorpay.Client(auth=("<YOUR_API_KEY>", "<YOUR_API_SECRET>"))
```

You can find your API keys at <https://dashboard.razorpay.com/#/app/keys>.

The most common construct is capturing payments, which you do via the following:

```py
razor.payment.capture("<PAYMENT_ID>")
```
