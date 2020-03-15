import os # Run OS-specific commands

class Dispatcher:
    def __init__(self):
        self.dispatchTable = {
            "docx" : self.openDocx,
            "txt" : self.openTxt,
            "mp3" : self.openMp3, 
            "html" : self.openHtml
        }

    def openDocx(self, fileName):
        os.system(f"start winword {fileName}")

    def openTxt(self, fileName):
        os.system(f"start notepad {fileName}")

    def openMp3(self, fileName):
        os.system(f"start wmplayer {fileName}")

    def openHtml(self, fileName):
        os.system(f"start firefox {fileName}")

    def dispatch(self, fileName, fileExtension):
        self.dispatchTable.get(fileExtension)(fileName)