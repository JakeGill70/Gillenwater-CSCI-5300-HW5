# Jake Gillenwater
# Gillenwaterj@etsu.edu

import sys # Access command line arguments
import os.path # Inquire information about a supposed file path
 # Access all of the different types of file extension handlers for the CoR pattern
from Handler.Docx import Handler_docx
from Handler.Html import Handler_html
from Handler.Mp3 import Handler_mp3
from Handler.Txt import Handler_txt

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

        # Create instances of all of the different handlers
        docx = Handler_docx()
        html = Handler_html()
        mp3 =  Handler_mp3()
        txt =  Handler_txt()

        # Establish the chain of responsibility
        docx.setNextHandler(html)
        html.setNextHandler(mp3)
        mp3.setNextHandler(txt)

        # Send a message down the chain
        docx.checkRequest((fileName, fileExtension))
        
if __name__ == "__main__":
    Driver.main()