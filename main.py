import os
import logging
import random
import asyncio
import ssl as ssl_lib

import certifi
import slack
import requests

# ================ Team Join Event =============== #
# When the user first joins a team, the type of the event will be 'team_join'.
# Here we'll link the onboarding_message callback to the 'team_join' event.
@slack.RTMClient.run_on(event="team_join")
async def onboarding_message(**payload):
    """Create and send an onboarding welcome message to new users. Save the
    time stamp of this message so we can update this message in the future.
    """
    # Get WebClient so you can communicate back to Slack.
    web_client = payload["web_client"]

    # Get the id of the Slack user associated with the incoming event
    user_id = payload["data"]["user"]["id"]

    # Open a DM with the new user.
    response = web_client.im_open(user_id)
    channel = response["channel"]["id"]

    # Post the onboarding message.
    web_client.chat_postMessage(channel=channel, text="Welcome to the BEAM Slack!")

# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@slack.RTMClient.run_on(event="message")
async def message(**payload):

    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    text = data.get("text")

    if "!minecraft" in text:
        web_client.chat_postMessage(channel=channel_id, text="Minecraft is a great game. If you want to join a server with other people from BEAM, DM Nikhil for an invite.")
    elif "i am " in text.lower() or "i'm " in text.lower():
        target_word = text.split("am ")[1] if ("I am " in text) else text.split("I'm ")[1]
        web_client.chat_postMessage(channel=channel_id, text="Hi " + target_word + ", my name is Beam Bot!")
    elif "never gonna give you up" in text.lower():
        web_client.chat_postMessage(channel=channel_id, text="Never gonna let you down.")
    elif "estoy aburrido" in text.lower():
        choice = random.randint(1, 3)
        if choice == 1:
            web_client.chat_postMessage(channel=channel_id, text="Why not play minecraft? !minecraft for more.")
        if choice == 2:
            web_client.chat_postMessage(channel=channel_id, text="Here's a neat article for you to read: http://www.latlmes.com/arts/return-of-the-golden-age-of-comics-1")
        if choice == 3:
            web_client.chat_postMessage(channel=channel_id, text="Me too.")
    elif "tell me a joke" in text.lower():
        joke = str(requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"}).json()["joke"])
        web_client.chat_postMessage(channel=channel_id, text=joke)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    slack_token = os.environ.get('SLACK_BOT_TOKEN')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    rtm_client = slack.RTMClient(
        token=slack_token, ssl=ssl_context, run_async=True, loop=loop
    )
    loop.run_until_complete(rtm_client.start())
