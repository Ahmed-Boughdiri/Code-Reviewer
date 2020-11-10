
class Indentation:
    def __init__(self):
        pass
    def isAnIndentation(self,keyword):
        if "    " in keyword or "   " in keyword:
            return True
        return False
