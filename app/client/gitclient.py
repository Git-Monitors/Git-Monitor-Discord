import discord
import logging

class GitClient(discord.Client):
    async def on_ready(self : discord.Client):
        logging.info(f"Logged in as f{self.user}")

    async def on_message(self, message : discord.Message):
        if message.author == self.user:
            return

        if message.content.startswith("$hello"):
            await message.channel.send("Hello! Git-Bot here.")

    async def on_update_event(self, event : str, description : str, url : str, receipients : int):
        await self.get_channel(receipients).send(f"Event: {event}, Description: {description}, Url: {url}, Receipients: {receipients}")

    