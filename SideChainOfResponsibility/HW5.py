# Jake Gillenwater
# Gillenwaterj@etsu.edu

import sys # Access command line arguments
import os.path # Inquire information about a supposed file path
<<<<<<< HEAD:Switch/HW5.py
from Handler.Dispatcher import Dispatcher # Used to open the file with the appropriate program
=======
 # Access all of the different types of file extension handlers for the CoR pattern
from Handler.Docx import Handler_Docx
from Handler.Html import Handler_Html
from Handler.Mp3 import Handler_Mp3
from Handler.Txt import Handler_Txt
>>>>>>> SideChainCoR:SideChainOfResponsibility/HW5.py

class Driver:
    acceptedExtensions = ["docx", "mp3", "html", "txt"]

    @staticmethod
    def main():
        # Get the file name from the list of command line arguments
        try:
            fileName = sys.argv[1]
        except:
            # If the file does not exists, then no further operations
            # can be performed, so the program should close itself.
            print("No argument provided. Please include the name of the file that you would like to open.")
            exit()

        # Make sure that the file exists
        if( not os.path.isfile(fileName)):
            # If the file does not exists, then no further operations
            # can be performed, so the program should close itself.
            print("File could not be found.")
            exit()

        # Ensure that the path is absolute, not local, so that
        # other applications are not confused about where the file is.
        fileName = os.path.abspath(fileName)
        print(fileName)

        # Get the file's extension
        fileExtension = Driver.getFileExtension(fileName)
        if(fileExtension == ""):
            # If the file has no extension, then no further operations
            # can be performed, so the program should close itself.
            print("File extension could not be determined.")
            exit()

        # Check to make sure the file extension is recognized
        if(fileExtension not in Driver.acceptedExtensions):
             # If the file extension is not recognized, then no further operations
            # can be performed, so the program should close itself.
            print(f"File extension .{fileExtension} is unknown.")
            exit()
        
        # Launch the appropriate app based on the file extension
        Driver.openFileInApplication(fileName, fileExtension)

    @staticmethod
    def getFileExtension(fileName):
        try:
            fileExtension = fileName.split(".")[-1]
        except IndexError:
            fileExtension = ""
        return fileExtension

    @staticmethod
    def openFileInApplication(fileName, fileExtension):
<<<<<<< HEAD:Switch/HW5.py
        dispatcher = Dispatcher()
        dispatcher.dispatch(fileName, fileExtension)
=======

        # Create instances of all of the different handlers
        #   and Establish the chain of responsibility
        chainOfResponsibility = Handler_Docx(Handler_Html(Handler_Mp3(Handler_Txt())))

        # Send a message down the chain
        chainOfResponsibility.checkRequest((fileName, fileExtension))
>>>>>>> SideChainCoR:SideChainOfResponsibility/HW5.py
        
if __name__ == "__main__":
    Driver.main()