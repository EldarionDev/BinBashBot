class Help:
    def __init__(self):
        self.helpFile = open("assets/help.txt")
        self.helpText = self.helpFile.readlines()

    async def printHelp(self, message):
        out = ""
        for line in self.helpText:
            out = out + line + "\n"
        await message.author.send(out)
        return
