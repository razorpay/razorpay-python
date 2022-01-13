import razorpay
import requests
from pprint import pprint
import json

client = razorpay.Client(auth=("rzp_test_k6uL897VPBz20q", "EnLs21M47BllR3X8PSFtjtbd"))


DATA = {
  "type": "bank_account",
  "bank_account": {
    "ifsc": "UTIB0000013",
    "account_number": "914010012345679"
  }
}
       
# sig = '07ae18789e35093e51d0a491eb9922646f3f82773547e5b0f67ee3f2d3bf7d5b'
# parameters = {}
# parameters['razorpay_payment_id'] = 'pay_IH3d0ara9bSsjQ'
# parameters['payment_link_id'] = 'plink_IH3cNucfVEgV68'
# parameters['payment_link_reference_id'] = 'TSsd1989'
# parameters['payment_link_status'] = 'paid'
# parameters['razorpay_signature'] = sig

#x = client.subscription.delete_offer('sub_IjA0wMVJdFnyzx','offer_IjA06IHSz33cw2')
#response = json.load(x)
#print(x)
# if(x==''):
#   return True
# else:
#   return False  
