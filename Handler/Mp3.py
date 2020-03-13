from Handler.File import Handler_File # Used for inheritance
import os # Run OS-specific commands

class Handler_mp3(Handler_File):
    def __init__(self):
        self.setNextHandler(None)
        self.myExtension = "mp3"
    def processRequest(self, arg:(str, str)):
        os.system(f"start wmplayer {arg[0]}")