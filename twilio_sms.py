from twilio.rest import TwilioRestClient

account_sid = "AC0e4860d6319ee7ad545eef595a457f5e" # Your Account SID from www.twilio.com/console
auth_token  = "f13d378d6180ad7a21bb3a842cdf9454"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+917848074059",    # Replace with your phone number
    from_="+12345678901") # Replace with your Twilio number

print(message.sid)
