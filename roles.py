import os


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
                for j in currentContent:
                    if j == "help.txt":
                        continue
                    string = string + "**" + j + "**" + "\n"
                out = infoText + capitalText + string
                await message.channel.send(out)
                return
