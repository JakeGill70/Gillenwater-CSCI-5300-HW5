from Handler.File import Handler_File # Used for inheritance
import os # Run OS-specific commands

class Handler_Txt(Handler_File):
<<<<<<< HEAD:SimpleChainOfResponsibility/Handler/Txt.py
    def __init__(self):
        self.setNextHandler(None)
=======
    def __init__(self, nextHandler=None):
        self.setNextHandler(nextHandler)
>>>>>>> ConstructorHardCoR:ConstructorChainOfResponsibility/Handler/Txt.py
        self.myExtension = "txt"
    def processRequest(self, arg:(str, str)):
        os.system(f"start notepad {arg[0]}")