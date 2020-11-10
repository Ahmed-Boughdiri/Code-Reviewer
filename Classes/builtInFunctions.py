
class BuiltInFunctions:
    def __init__(self):
        pass
    def isBuiltInFunction(self,keyword):
        if ("len(" in keyword or "split(" in keyword):
            return True
        return False
