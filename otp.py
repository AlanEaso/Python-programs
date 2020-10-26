#A simole OTP Generator using random
#For this to work one should have a twilio account. It's free for trial runs

from random import *
from twilio.rest import Client

otp = randint(1000,10000)
print(otp)
asid = ''  #account sid from twilio account
atoken= '' #from twilio account
cl = Client(asid,atoken)
message = cl.messages.create(
    body='Your otp is '+str(otp),
    from_= '' , #trial number you get from twilio
    to=''
)

print(message.sid)
