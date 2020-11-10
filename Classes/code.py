from Classes.codeData import CodeData
from Functions.countKeywords import count_keywords

class Code:
    def __init__(self,code):
        self.code = code
    def split(self):
        self.codeSource = self.code.split("\n")
        #TODO: Delete strings inside the code 
        for index,item in enumerate(self.codeSource):
            while "'" in item or '"' in item:
                if '"' in item:
                    start = item.find('"')
                    item = item[:start] + item[start+1:]
                    end = item.find('"')
                    item = item[:start] + item[end+1:]
                    self.codeSource[index] = item

                elif "'" in item:
                    start = item.find("'")
                    item = item[:start] + item[start+1:]
                    end = item.find("'")
                    item = item[:start] + item[end+1:]
                    self.codeSource[index] = item
            

    def splitKeywork(self):
        result = []
        for item in self.codeSource:    
            keywords = item.split(" ")
            #TODO: Delete empty lines
            result.append(keywords)
        self.codeSource = result

    def analyzeLine(self,line,codeInfo,*args,**kwargs):
        for index,keyword in enumerate(line):
            count_keywords(keyword,codeInfo,line=line,lineNumber=kwargs["lineNumber"],keywordIndex=index,codeSource=kwargs["codeSource"])
            

    def analyze(self):
        codeInfo = CodeData()
        for index,item in enumerate(self.codeSource):
            codeInfo.lines_of_code = len(self.codeSource)
            self.analyzeLine(item,codeInfo,lineNumber=index,codeSource=self.codeSource)
        return codeInfo
        
