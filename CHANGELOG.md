# Change Log

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## [1.3.0][1.3.0] - 2022-01-17

### Added
- Added Item Api
- Added RegistrationLink Api
- QR code end point API
- Update, cancel update ,fetch details of a Pending Update, pause, resume subscription & delete offer API
- Add create ondemand , fetch all demand, fetch demand by id & report for settlement 
- Add/Delete TPV Bank Account 
- Register emandate and charge first payment together 
- PaperNACH/Register NACH and charge first payment together 
- Added create recurring payment, fetch card details, card downtime & card downtime by Id , create payment json API's for payment
- Added edit and notify API's for payment links 
- Added edit, refund, fetch multiple refund, fetch multiple refund by id API's for refunds 
- Added edit order API 
- Fund API's end point 
- UPI 
- Added Verfiy payment link ,payment & subscription verification 
- Update Testcases
- Update readme file 

## [1.2.0][1.2.0] - 2019-03-11

### Added

-   New Settlement read APIs [[#61](https://github.com/razorpay/razorpay-python/pull/61)]
-   New APIs for Invoices (Issue/Delete/(re)Send/Edit/Cancel) [[#61](https://github.com/razorpay/razorpay-python/pull/61)]
-   New APIs for Payment Links ((re)Send Notification/Cancel) [[#61](https://github.com/razorpay/razorpay-python/pull/61)]

## [1.1.1][1.1.1] - 2018-01-15

### Added

-   Added supported python versions in `setup.py` and README

## [1.1.0][1.1.0] - 2017-10-26

### Added

-   Added Client for Virtual Account, Transfer, Subscriptions

## [1.0.2][1.0.2] - 2017-07-31

### Fixed

-   Webhook signature verification
-   Added support for python ver < 2.7.7

## [1.0.1][1.0.1] - 2017-04-03

### Added

-   Adds support for setting application details in the user-agent header

## [1.0.0][1.0.0] - 2017-03-10

### Added

-   Added Support For Signature Validation
-   Added Client for Card, Customer, Token
-   Now Sdk throws BadRequestError, GatewayError, ServerError, SignatureVerificationError depending on error occurred
-   Set Base URL of API on client level instead of request level
-   Updated README
-   Supports Notes for Order and Refund, and line itmes in Invoices

### Changed

-   Refund Can be fetched by just refund id, previously it needed payment id also
-   Test Coverage Increased to 100%
-   Deprecated fetch_all in favour of all
-   Take params in a dictonary instead of key/value pair

## [0.2.0][0.2.0] - 2016-07-04

### Added

-   API for Orders.
-   Return Proper Error Message
-   docstring for all API

## [0.1.0][0.1.0] - 2015-11-19

### Added

-   Tests: For payments and refunds.

### Changed

-   **data** argument to create refund is now optional.
-   Add mandatory **amount** argument for payment capture.

### Fixes

-   Local imports for py 3.x.

## [0.1.0-alpha] - 2015-11-18

### Added

-   Payments: List, fetch and capture payments.
-   Refunds: List, fetch and initiate refunds.

[unreleased]: https://github.com/razorpay/razorpay-python/compare/1.2.0...HEAD
[1.2.0]: https://github.com/razorpay/razorpay-python/compare/1.1.1...1.2.0
[1.1.1]: https://github.com/razorpay/razorpay-python/compare/1.1.0...1.1.1
[1.1.0]: https://github.com/razorpay/razorpay-python/compare/1.0.2...1.1.0
[1.0.2]: https://github.com/razorpay/razorpay-python/compare/1.0.1...1.0.2
[1.0.1]: https://github.com/razorpay/razorpay-python/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/razorpay/razorpay-python/compare/0.2.0...1.0.0
[0.2.0]: https://github.com/razorpay/razorpay-python/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/razorpay/razorpay-python/compare/0.1.0-alpha...0.1.0
