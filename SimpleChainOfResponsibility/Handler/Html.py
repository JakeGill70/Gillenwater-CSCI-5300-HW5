from Handler.File import Handler_File # Used for inheritance
import os # Run OS-specific commands

class Handler_Html(Handler_File):
    def __init__(self):
        self.setNextHandler(None)
        self.myExtension = "html"
    def processRequest(self, arg:(str, str)):
        os.system(f"start firefox {arg[0]}")