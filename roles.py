import os

import discord


class User:
    def __init__(self, name):
        self.name = name
        self.currentDir = ""

    def setCurrentDir(self, currentDir):
        self.currentDir = currentDir

    def getCurrentDir(self):
        return self.currentDir


class Roles:
    def __init__(self):
        print("Roles initialized.")
        self.currentUserCount = 0
        self.userList = []

    def addUser(self, message):
        self.userList.append(User(message.author))
        self.userList[self.currentUserCount].setCurrentDir("assets/")
        self.currentUserCount = self.currentUserCount + 1

    def removeUser(self, message):
        i = 0
        while i < self.currentUserCount:
            if self.userList[i].name == message.author:
                self.userList[i].name = ""
                return

    def addDir(self, message, dirName):
        i = 0
        while i < self.currentUserCount:
            if self.userList[i].name == message.author:
                newPath = self.userList[i].currentDir + dirName + "/"
                self.userList[i].currentDir = newPath
                return
            i = i + 1

    async def removeRole(self, message):
        content = message.content.split(" ")
        roleName = content[3]
        role = discord.utils.get(message.guild.roles, name=roleName)
        try:
            await message.author.remove_roles(role)
        except:
            await message.channel.send("The role you entered is not existing")

    async def addRole(self, message):
        content = message.content.split(" ")
        roleName = content[3]
        role = discord.utils.get(message.guild.roles, name=roleName)
        try:
            await message.author.add_roles(role)
        except:
            await message.channel.send("The role you entered is not existing")

    async def printDir(self, message):
        i = 0
        while i < self.currentUserCount:
            if self.userList[i].name == message.author:
                currentContent = os.listdir(self.userList[i].getCurrentDir())
                infoText = ("Use *bbb roles add* to add a role. \n"
                            "Use *bbb roles stop* to stop this dialog. \n"
                            "Use *bbb roles enter* to enter a role directory.\n"
                            "Use *bbb roles remove* to remove a role.\n")
                capitalText = "**THE ROLES IN THIS DIRECTORY:**\n"
                string = ""
                out = ""
                for j in currentContent:
                    if j == "help.txt":
                        continue
                    if os.path.isfile(self.userList[i].getCurrentDir() + j):
                        string = string + "**" + j + "**" + " *(Role)*" + "\n"
                    else:
                        string = string = string + "**" + j + "**" + " *(Directory + Role)*" + "\n"
                out = infoText + capitalText + string
                if out == "":
                    await message.channel.send("The requested role directory could not be found!")
                    return
                await message.channel.send(out)
                return
