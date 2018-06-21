
class sortFile(object):

    
    def __init__(self,fileDict):
        self.fileDict = fileDict


    def sort(self):
        pass

class sortWithName(sortFile):

    
    def __init__(self, fileDict):
        super().__init__(fileDict)


    def sort(self):
        k = sorted(self.fileDict.items(), key=lambda x: x[1]['fileName'], reverse=True)
        return dict(k)

class sortWithTime(sortFile):

    def __init__(self, fileDict):
        super().__init__(fileDict)


    def sort(self):
        k = sorted(self.fileDict.items(), key=lambda x: x[1]['fileTime'], reverse=True)
        return dict(k)

class sortWithSize(sortFile):

    def __init__(self, fileDict):
        super().__init__(fileDict)


    def sort(self):
        k = sorted(self.fileDict.items(), key=lambda x: float(x[1]['fileSize'][:-2]), reverse=True)
        return dict(k)


