import random
import os
from twilio.rest import Client
otp = random.randint(10000,99999)
account_sid= "ACd81a4ef67e08078f0728f6b369f9d231"
auth_token= '75bda874ca070490944a45433624dde6'
client = Client(account_sid,auth_token)
msg=client.messages.create(
    body = f"Your OTP is {otp}",
    from_="+12186751553",
    to ="+916380680741"

    )
