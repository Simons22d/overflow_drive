import requests
from requests.auth import HTTPBasicAuth
from base64 import b64encode
from datetime import datetime
import logging
import os
# denis
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")

def authenticate():
    """
    :return: MPESA_TOKEN
    """
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    return r.text


def stk_push(token, business_shortcode, lipa_na_mpesapasskey, amount, party_a, phonenumber,callbackurl):
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % token}
    timestamp = datetime.now().strftime("%Y%m%d%I%M%S")
    pswd = (business_shortcode + lipa_na_mpesapasskey + timestamp).encode("utf-8")
    password = b64encode(pswd).decode()
    req = {
        "BusinessShortCode": "174379",
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": party_a,
        "PartyB": business_shortcode,
        "PhoneNumber": phonenumber,
        "CallBackURL": callbackurl,
        "AccountReference": business_shortcode,
        "TransactionDesc": "test",
    }
    response = requests.post(api_url, json=req, headers=headers)
    logging.info("response",response)
    return response
