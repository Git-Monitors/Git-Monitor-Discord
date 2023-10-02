import discord
import logging

class GitClient(discord.Client):
    async def on_ready(self : discord.Client):
        logging.info(f"Logged in as f{self.user}")

    async def on_message(self, message : discord.Message):
        if message.author == self.user:
            return

        if message.content.startswith("$hello"):
            await message.channel.send("Hello!")