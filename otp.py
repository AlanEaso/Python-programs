#A simole OTP Generator using random

from random import *
from twilio.rest import Client

otp = randint(1000,10000)
print(otp)
asid = 'AC1419730200772fd1dd0764c9eb977d5d'
atoken= '059a9f16d2892e37ec39a212ef827ffd'
cl = Client(asid,atoken)
message = cl.messages.create(
    body='Your otp is '+str(otp),
    from_= '+12566662802' ,
    to='+918547442300'
)

print(message.sid)