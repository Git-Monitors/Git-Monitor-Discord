import os
import discord
from gitclient import GitClient
from dotenv import load_dotenv
import logging

load_dotenv()

if __name__=="__main__" :
    token = os.getenv("DISCORD_APP_TOKEN")
    assert token is not None, "DISCORD_APP_TOKEN is not set"
    assert len(token) > 0, "DISCORD_APP_TOKEN is empty"

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    try:
        client = GitClient(intents=intents)
        client.run(token)
    except Exception as e:
        logging.error(e)
        