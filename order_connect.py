import razorpay
import logging
import http.client as http_client
import time
import random
import os


# Enable HTTP debugging
# http_client.HTTPConnection.debuglevel = 1
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

api_key = os.getenv('RZP_API_KEY')
api_secret = os.getenv('RZP_API_SECRET')

if not api_key or not api_secret:
    raise ValueError("Please set RZP_API_KEY and RZP_API_SECRET environment variables")

client = razorpay.Client(auth=(api_key, api_secret))


for i in range(15):
    try:
        x = client.order.create({
          "amount": 50000,
          "currency": "INR",
          "receipt": f"receipt#{i+1}",
          "partial_payment":False,
          "notes": {
            "key1": "value3",
            "key2": "value2"
          }
        })
        
        print(f"Request {i+1}/15 at {time.strftime('%Y-%m-%d %H:%M:%S')}: {x}")
        
    except Exception as e:
        print(f"Error in request {i+1}/15: {e}")
    
    # Random delay between 1-5 seconds (skip delay after last request)
    if i < 14:
        delay = random.uniform(1, 5)
        print(f"Waiting {delay:.1f} seconds...")
        time.sleep(delay)

print("Completed all 15 requests!")
