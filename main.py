import discord
import os
from dotenv import load_dotenv
import help
import roles

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

helpInstance = help.Help()
roleInstance = roles.Roles()


class BinBashBotClient(discord.Client):
    async def on_ready(self):
        print("Connected to Linux/BSD Gaming Discord!")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith("bbb help"):
            await helpInstance.printHelp(message)
            return
        if message.content.startswith("bbb roles enter"):
            content = message.content.split(" ")
            roleInstance.addDir(message, content[3])
            await roleInstance.printDir(message)
            return
        if message.content.startswith("bbb roles stop"):
            roleInstance.removeUser(message)
            return
        if message.content.startswith("bbb roles add"):
            await roleInstance.addRole(message)
            return
        if message.content.startswith("bbb roles remove"):
            await roleInstance.removeRole(message)
            return
        if message.content.startswith("bbb roles"):
            roleInstance.addUser(message)
            await roleInstance.printDir(message)
            return
        if message.content.startswith("bbb ping"):
            await message.channel.send("Pong")
        if message.content.startswith("bbb"):
            await message.channel.send("I am a slave of your will. If you need help simply type bbb help and I'll "
                                       "immediately serve you!")
            return


client = BinBashBotClient()
client.run(TOKEN)
