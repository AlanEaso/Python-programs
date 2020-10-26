#A simole OTP Generator using random

from random import *
from twilio.rest import Client

otp = randint(1000,10000)
print(otp)
asid = ''
atoken= ''
cl = Client(asid,atoken)
message = cl.messages.create(
    body='Your otp is '+str(otp),
    from_= '' ,
    to=''
)

print(message.sid)
