import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

helpFile = open('assets/help.txt', 'r')
helpText = helpFile.readlines()


class BinBashBotClient(discord.Client):
    async def on_ready(self):
        print("Connected to Linux/BSD Gaming Discord!")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith("bbb help"):
            for line in helpText:
                await message.author.send(line)
            return
        if message.content.startswith("bbb"):
            await message.channel.send("I am a slave of your will. If you need help simply type bbb help and I'll "
                                       "immediately serve you!")
            return


client = BinBashBotClient()
client.run(TOKEN)
