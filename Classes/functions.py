
class Function:
    def __init__(self):
        pass
    def isFunction(self,keyword):
        if "def" in keyword:
            return True
        return False
    def increase_functions_count(self, codeInfo):
        codeInfo.functions += 1
