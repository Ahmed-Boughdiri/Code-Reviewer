
class Assign:
    def __init__(self):
        pass
    def isAnAssignOperator(self, keyword):
        if "=" in keyword:
            return True
        return False
