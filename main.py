import os
import discord
from gitclient import GitClient
from dotenv import load_dotenv
import logging
from typing import Union
from fastapi import FastAPI
import asyncio
from pydantic import BaseModel

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
    return {"Hello": "World"}

class Updates(BaseModel):
    EventType: str
    EventDescription: str 
    EventUrl : str
    EventReceipients : int

@app.post("/eventupdates")
async def post_event_updates(updates: Updates):
    await client.on_update_event(updates.EventType, updates.EventDescription, updates.EventUrl, updates.EventReceipients)
    return updates

        