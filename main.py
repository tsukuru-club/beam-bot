import os
import logging
import random
import asyncio
import ssl as ssl_lib

import certifi
import slack
import messages

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

    reply = messages.processMessage(text)
    if reply:
        web_client.chat_postMessage(channel=channel_id, text=reply)

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
