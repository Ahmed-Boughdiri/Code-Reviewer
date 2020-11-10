
class Class:
    def __init__(self):
        pass
    def isClass(self,keyword):
        if "class" in keyword:
            return True
        return False
    def isClassProperty(self,keyword):
        if "self." in keyword:
            return True
        return False
