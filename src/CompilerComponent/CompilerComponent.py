class CompilerComponent:
    def __init__(self, text : str = None, ast = None):
        self.ast = ast
        self.errors = []
        self.text = text

    def Execute(self):
        #Execute the component
        pass

    def GetErrors(self):
        #Get errors from execution
        pass
    