from Handler.File import Handler_File # Used for inheritance
import os # Run OS-specific commands
 # Access all of the different types of file extension handlers for the CoR pattern
from Handler.Docx_LibreWriter import Handler_Docx_LibreWriter
from Handler.Docx_MSWord import Handler_Docx_MSWord
from Handler.Docx_MSWordpad import Handler_Docx_MSWordpad

class Handler_Docx(Handler_File):
    def __init__(self, nextHandler=None):
        self.setNextHandler(nextHandler)
        self.myExtension = "docx"
    def processRequest(self, arg:(str, str)):
        SideChainOfResponsibility = Handler_Docx_MSWord(Handler_Docx_LibreWriter(Handler_Docx_MSWordpad()))
        SideChainOfResponsibility.checkRequest(arg)