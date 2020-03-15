class Handler_Abstract:
    def __init__(self):
        self.setNextHandler(None)
    def setNextHandler(self, handler):
        self.nextHandler = handler
    def getNextHandler(self):
        return self.nextHandler
    def passRequest(self, arg):
        self.nextHandler.checkRequest(arg)
    def checkRequest(self, arg):
        pass
    def processRequest(self, arg):
        pass