from twilio import rest

account_sid = "AC55fcfd861a8233e055f95bf902ccd26d" # Your Account SID from www.twilio.com/console
auth_token  = "eb74dbf16af03389bfc88597c77eec64"

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello, this is me!",
    to="+15712061007",    # Replace with your phone number
    from_="+15514974268") # Replace with your Twilio number

print(message.sid)



#Sethdo1297
