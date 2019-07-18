import messages

reply = messages.processMessage("get price of DOGE in USD")
if reply:
    print(reply)