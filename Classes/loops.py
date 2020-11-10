
class Loop:
    def __init__(self):
        pass
    def isForLoop(self,keyword):
        if "for" in keyword:
            return True
        return False
    def isWhileLoop(self,keyword):
        if "while" in keyword:
            return True
        return False
