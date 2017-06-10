from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "AC99cfd366abd9d8701e9748a216c930b7"
# Your Auth Token from twilio.com/console
auth_token  = "691b9c32ccd4e81ad9f8ef2ba7cfddc2"

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    to="+919662550290", 
    from_="+18562194547 ",
    body="My Name is Viren Parmar?")

print(message.sid)