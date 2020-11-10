
class ImportStatement:
    def __init__(self):
        pass
    def isAnImport(self,keyword):
        if "import" in keyword:
            return True
        return False
