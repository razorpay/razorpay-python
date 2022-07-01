import razorpay
import requests
from pprint import pprint
import json

client = razorpay.Client(auth=("rzp_test_k6uL897VPBz20q", "EnLs21M47BllR3X8PSFtjtbd"))

data = {"customer_id":"cust_JnFmpXS63vWgYJ"}

#x = client.addon.delete("ao_JniYt836HF7aQm")

x = client.transfer.all({
  'expand[]':'recipient_settlement'  
})

print(json.dumps(x))

    # def delete(self, addon_id, data={}, **kwargs):
    #     """
    #     Delete addon for given id

    #     Args:
    #         addon_id : Id for which addon object has to be deleted
    #     """
    #     url = '{}/{}'.format(self.base_url, addon_id)

    #     return self.delete_url(url, data, **kwargs)
# "please check response error_code , error_desc , tax and other are missing
# tested with account va_JccSJQQoGOBi2q"