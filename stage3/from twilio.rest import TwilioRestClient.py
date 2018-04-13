from twilio.rest import TwilioRestClient

account_sid = "AC5c7b972aa2c033e9ee62a92a0924beed" # Your Account SID from www.twilio.com/console
auth_token  = "7c972e110df05e3fbed3f1527e5da8e7"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="guess who i am",
    to="+17854243227",    # Replace with your phone number
    from_="+17857277234") # Replace with your Twilio number

print(message.sid)