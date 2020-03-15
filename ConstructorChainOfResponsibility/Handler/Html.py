from Handler.File import Handler_File # Used for inheritance
import os # Run OS-specific commands

class Handler_Html(Handler_File):
<<<<<<< HEAD:SimpleChainOfResponsibility/Handler/Html.py
    def __init__(self):
        self.setNextHandler(None)
=======
    def __init__(self, nextHandler=None):
        self.setNextHandler(nextHandler)
>>>>>>> ConstructorHardCoR:ConstructorChainOfResponsibility/Handler/Html.py
        self.myExtension = "html"
    def processRequest(self, arg:(str, str)):
        os.system(f"start firefox {arg[0]}")