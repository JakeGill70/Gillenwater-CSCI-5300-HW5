from Handler.File import Handler_File # Used for inheritance
import os # Run OS-specific commands

class Handler_Txt(Handler_File):
    def __init__(self, nextHandler=None):
        self.setNextHandler(nextHandler)
        self.myExtension = "txt"
    def processRequest(self, arg:(str, str)):
        os.system(f"start notepad {arg[0]}")