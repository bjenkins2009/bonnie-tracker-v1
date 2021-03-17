import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

slack_token = os.getenv('xoxb_token')
client = WebClient(token=slack_token)

def slack_message(text="", channel="#walks", ):
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=text
        )
        return response
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]