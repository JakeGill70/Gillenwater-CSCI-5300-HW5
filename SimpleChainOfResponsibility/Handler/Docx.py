from Handler.File import Handler_File # Used for inheritance
import os # Run OS-specific commands

class Handler_Docx(Handler_File):
    def __init__(self):
        self.setNextHandler(None)
        self.myExtension = "docx"
    def processRequest(self, arg:(str, str)):
        os.system(f"start winword {arg[0]}")