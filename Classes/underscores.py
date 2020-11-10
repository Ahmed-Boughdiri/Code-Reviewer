
class Underscores:
    def __init__(self):
        pass
    def isAnUnderscore(self,keyword):
        if "_" in keyword:
            return True
        return False
    def isDoubleUnderscores(self,keyword):
        if "__" in keyword:
            return True
        return False
