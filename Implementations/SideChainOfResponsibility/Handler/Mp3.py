from Handler.File import Handler_File # Used for inheritance
import os # Run OS-specific commands

class Handler_Mp3(Handler_File):
    def __init__(self, nextHandler=None):
        self.setNextHandler(nextHandler)
        self.myExtension = "mp3"
    def processRequest(self, arg:(str, str)):
        os.system(f"start wmplayer {arg[0]}")