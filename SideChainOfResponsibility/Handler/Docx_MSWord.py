from Handler.File import Handler_File # Used for inheritance
import os # Run OS-specific commands

class Handler_Docx_MSWord(Handler_File):
    def __init__(self, nextHandler=None):
        self.setNextHandler(nextHandler)
        self.myExtension = "docx"
    def checkRequest(self, arg:(str, str)):
        # Just pass the buck on this because the check is during
        # after attempting to process.
        self.processRequest(arg)
    def processRequest(self, arg:(str, str)):
        successful = (os.system(f"start winword {arg[0]}") == 0)
        if not successful :
            self.passRequest(arg)