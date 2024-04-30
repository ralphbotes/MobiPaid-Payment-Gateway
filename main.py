import requests
import json

def paymentRequest(a_url,a_prefix,a_key):
    payload = json.dumps( {
        "request_methods": [ "SMS"],
        "reference_number": "123",
        "email": "example@example.com",
        "merchant_phone_number": None,
        "mobile_number": "+12345678901",  
        "customer_salutation": "Mr",
        "customer_first_name": "John",
        "customer_last_name" : "Preston",
        "redirect_url" : "https://mobipaid.com",
        "response_url" : "https://mobipaid.com",
        "cancel_url" : "https://mobipaid.com",
        "fixed_amount": True,
        "currency": "ZAR",
        "amount": 1500.12,
        "moto_enabled": False, 
        "shipping_enabled": False, 
        "send_mms_invoice": True,
        "attach_invoice": True,
        "invoice_url": "https://mp-fixed-assets.s3.amazonaws.com/logo.png",
        "attach_receipt": True, 
        "receipt_file_type": "pdf",
        "payment_type": "DB",
        "payment_frequency": "ONE-TIME"
    } )
    
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {a_prefix + a_key}"
    }

    response = requests.request("POST", a_url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

def main(a_live):
    url = "https://test.mobipaid.io/v2/payment-requests"
    prefix = "mp_test_"
    key = "V015IU6m19HLDimH9F7A"

    if a_live:
        url = "https://live.mobipaid.io/v2/payment-requests"
        prefix = "mp_live_"
        key = ""
    
    paymentRequest(url,prefix,key)

if "__main__" == __name__:

    live = False
    main(live)