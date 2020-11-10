
class Braces:
    def __init__(self):
        pass
    def isBrackets(self,keyword):
        if "[]" in keyword or "[ ]" in keyword:
            return True
        return False
    def isCurlyBraces(self,keyword):
        if "{" in keyword:
            return True
        return False
