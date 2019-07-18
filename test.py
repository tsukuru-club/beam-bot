import messages

reply = messages.processMessage("get price of BTC in USD")
if reply:
    print(reply)

print(messages.processMessage("give me a random emoji"))
