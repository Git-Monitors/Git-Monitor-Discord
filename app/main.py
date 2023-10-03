import asyncio
import logging
import os

import discord
from dotenv import load_dotenv
from fastapi import FastAPI

from app.client.gitclient import GitClient
from app.schemas.updates import Updates

app = FastAPI()
load_dotenv()

token = os.getenv("DISCORD_APP_TOKEN")
assert token is not None, "DISCORD_APP_TOKEN is not set"
assert len(token) > 0, "DISCORD_APP_TOKEN is empty"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = GitClient(intents=intents)


@app.on_event("startup")
async def startup_event():
    logging.info("Starting up")
    asyncio.create_task(client.start(token))


@app.get("/")
async def read_root():
    logging.info("Received request on /")
    return {"Hello": "World"}


@app.post("/eventupdates")
async def post_event_updates(updates: Updates):
    logging.info(f"Received request on /eventupdates: {updates}")
    await client.on_update_event(updates.EventType, updates.EventDescription, updates.EventUrl, updates.EventReceipients)
    return updates
