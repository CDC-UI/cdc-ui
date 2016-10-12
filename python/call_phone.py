from twilio.rest import TwilioRestClient
from json import load

with open("logins.json", "r") as loginfile:
    logins = load(loginfile)
with open("numbers.json", "r") as numberfile:
    numbers = load(numberfile)

account_sid = logins["sid"]
auth_token = logins["token"]
client = TwilioRestClient(account_sid, auth_token)

call = client.calls.create(to=numbers["chris"],
                           from_=numbers["twilio"],
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)
