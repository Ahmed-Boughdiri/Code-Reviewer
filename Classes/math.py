
class Operators:
    def __init__(self):
        pass
    def isAnOperator(self,keyword):
        if "+" in keyword:
            return True
        elif "-" in keyword:
            return True
        elif "/" in keyword:
            return True
        elif "*" in keyword:
            return True
        return False
