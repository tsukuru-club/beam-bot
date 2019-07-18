import requests
import crypto
import emoji

def processMessage(text):
    if "!minecraft" in text:
        return "Minecraft is a great game. If you want to join a server with other people from BEAM, DM Nikhil for an invite."
    elif "i am " in text.lower()[0:8] or "i'm " in text.lower()[0:8]:
        target_word = text.split("am ")[1] if ("I am " in text) else text.split("I'm ")[1]
        return "Hi " + target_word + ", my name is Beam Bot!"
    elif "never gonna give you up" in text.lower():
        return "Never gonna let you down."
    elif "tell me a joke" in text.lower():
        return str(requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"}).json()["joke"])
    elif "high five" in text.lower():
        return "✋"
    elif "get price of " in text.lower():
        return crypto.message(text)
    elif "give me a random emoji" in text:
        return str(emoji.random_emoji(6)[0])
    return None
