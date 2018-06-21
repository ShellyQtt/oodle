from sortStrategy import  *
from File import *
class sortCriteriaDecorator(sortFile):
    def sort(self):
        pass

class sortNameDecorator(sortCriteriaDecorator):

    def __init__(self, fileDict, name):
        super().__init__(fileDict)
        self.name = name

    def sort(self):
        newSortFile = {}
        sortFile = self.fileDict.sort()
        for file in sortFile:
            if self.name in sortFile[file]['fileName']:
                newSortFile[file] = sortFile[file]

        return newSortFile

class sortTypeDecorator(sortCriteriaDecorator):

    def __init__(self, fileDict, type):
        super().__init__(fileDict)
        self.type = type


    def sort(self):

        newSortFile = {}
        sortFile = self.fileDict.sort()
        for file in sortFile:
            if self.type == sortFile[file]['fileType']:
                newSortFile[file] = sortFile[file]

        return newSortFile

