from Handler.File import Handler_File # Used for inheritance
import os # Run OS-specific commands

class Handler_Docx(Handler_File):
<<<<<<< HEAD:SimpleChainOfResponsibility/Handler/Docx.py
    def __init__(self):
        self.setNextHandler(None)
=======
    def __init__(self, nextHandler=None):
        self.setNextHandler(nextHandler)
>>>>>>> ConstructorHardCoR:ConstructorChainOfResponsibility/Handler/Docx.py
        self.myExtension = "docx"
    def processRequest(self, arg:(str, str)):
        os.system(f"start winword {arg[0]}")