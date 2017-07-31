# Change Log
All notable changes to this project will be documented in this file. This project adheres to [Semantic Versioning](http://semver.org/).

### Unreleased

## [1.0.2] - 2017-07-31
### Fixed
- Webhook signature verification
- Added support for python ver < 2.7.7

## [1.0.1] - 2017-04-03
### Added
- Adds support for setting application details in the user-agent header

## [1.0.0] - 2017-03-10
### Added
- Added Support For Signature Validation
- Added Client for Card, Customer, Token
- Now Sdk throws BadRequestError, GatewayError, ServerError, SignatureVerificationError depending on error occurred
- Set Base URL of API on client level instead of request level
- Updated README
- Supports Notes for Order and Refund, and line itmes in Invoices

### Changed
- Refund Can be fetched by just refund id, previously it needed payment id also
- Test Coverage Increased to 100%
- Deprecated fetch_all in favour of all
- Take params in a dictonary instead of key/value pair

## [0.2.0] - 2016-07-04
### Added
- API for Orders.
- Return Proper Error Message
- docstring for all API

## [0.1.0] - 2015-11-19
### Added
- Tests: For payments and refunds.

### Changed
- **data** argument to create refund is now optional.
- Add mandatory **amount** argument for payment capture.

### Fixes
- Local imports for py 3.x.

## [0.1.0-alpha] - 2015-11-18
### Added
- Payments: List, fetch and capture payments.
- Refunds: List, fetch and initiate refunds.
