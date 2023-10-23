import os
from twilio.rest import Client
import requests

res = requests.get("https://www.apple.com/shop/buyability-message?parts.0=FLJ03LL/A")
body = res.json()

if res.status_code != 200:
    print(str(res.status_code))
    exit(1)

if body['head']['status'] != '200':
    print(res.status_code)
    exit(1)

in_stock = body['body']['content']['buyabilityMessage']['sth']['FLJ03LL/A']['isBuyable']

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_API_KEY")
recipient = os.getenv("RECIPIENT_NUMBER")
sender = os.getenv("SENDER_NUMBER")
client = Client(account_sid, auth_token)

event_name = os.getenv("GITHUB_EVENT_NAME")

if not in_stock:
    # message = client.messages.create(
    #     to=recipient,
    #     from_=sender,
    #     body="iPhone 13 mini 512GB - Starlight is available!")
    # print(message.sid)
    print("In stock!")
    exit(2)
elif event_name == "pull_request" or event_name == 'workflow_dispatch':
    # message = client.messages.create(
    #     to=recipient,
    #     from_=sender,
    #     body="iPhone 13 mini 512GB - Starlight is not available :(")
    # print(message.sid)
    print("Not in stock")
else:
    print("Not in stock")
