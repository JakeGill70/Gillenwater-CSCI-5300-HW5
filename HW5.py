# Jake Gillenwater
# Gillenwaterj@etsu.edu

import sys # Access command line arguments
import os # Run OS-specific commands
import os.path # Inquire information about a supposed file path

class Driver:
    @staticmethod
    def main():
        # Get the file name from the list of command line arguments
        print(sys.argv[1])
        fileName = sys.argv[1]

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
        applicationName = ""
        if(fileExtension == "docx"):
            applicationName = "winword"
        elif(fileExtension == "txt"):
            applicationName = "notepad"
        elif(fileExtension == "mp3"):
            applicationName = "wmplayer"
        elif(fileExtension in ["htm", "html", "shtml", "xhtml"]):
            applicationName = "firefox"
        os.system(f"start {applicationName} {fileName}")
        
if __name__ == "__main__":
    Driver.main()