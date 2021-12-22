import razorpay
client = razorpay.Client(auth=("rzp_test_1DP5mmOlF5G5ag", "thisissupersecret"))

DATA = {

  "customer_id": "cust_IEfAt3ruD4OEzo",
  "account_type":"bank_account",
  "bank_account":{
    "name":"Gaurav Kumar",
    "account_number":"11214311215411",
    "ifsc":"HDFC0000053"
  }
}

x = client.fund_account.create(data=DATA)

#print(x)

