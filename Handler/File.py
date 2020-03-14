from Handler.Abstract import Handler_Abstract # Used for inheritance

# Forces argument to be a tuple of type (fileName:str, fileExtension:str).
# Introduces a new property called "myExtension".
# Uses the new property to complete the checkRequest method
#   such that this lineage will automatically process a request
#   if it the correct fileType, and automatically passRequest() if not.
class Handler_File(Handler_Abstract):
    def __init__(self, nextHandler=None):
        self.setNextHandler(nextHandler)
        self.myExtension = ""
    def passRequest(self, arg:(str, str)):
        if(self.getNextHandler() != None):
            self.getNextHandler().checkRequest(arg) 
    def checkRequest(self, arg:(str, str)):
        if(arg[1] == self.myExtension):
            self.processRequest(arg)
        else:
            self.passRequest(arg)
    def processRequest(self, arg:(str, str)):
        pass