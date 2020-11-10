
class Condition:
    def __init__(self):
        pass
    def isCondition(self, keyword):
        if "if" in keyword:
            return True
        elif "elif" in keyword:
            return True
        elif "else" in keyword:
            return True
        return False
