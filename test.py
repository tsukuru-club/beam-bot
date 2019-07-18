import messages

reply = messages.processMessage("get price of BTC in USD")
if reply:
    print(reply)