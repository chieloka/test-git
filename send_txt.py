from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC948140f5693e3d375193e6ee532d1732"
# Your Auth Token from twilio.com/console
auth_token  = "dfc47bece44e1099b6c935d6fce26a99"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+2348057928002", 
    from_="+12565884269",
    body="Hello from Python!")

print(message.sid)
