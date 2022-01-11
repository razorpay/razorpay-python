import razorpay
client = razorpay.Client(auth=("rzp_test_k6uL897VPBz20q", "EnLs21M47BllR3X8PSFtjtbd"))


DATA = {

  "quantity":2,
  "schedule_change_at":"cycle_end",

}
       

#x = client.invoice.all({'subscription_id':'sub_IaqsexdKtHj8Av'})
#print(x)