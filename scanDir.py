from sortDecorator import *
from modeFactory import *
timeId = '1'
sizeId = '2'
nameId = '3'
logId = '1'
compareId = '2'

class sortDir():
    def __init__(self, rootDir, selectCriteria, sortId):
        self.rootDir = rootDir
        self.selectCriteria = selectCriteria
        self.sortId = sortId

    def sort(self):
        fileDict = getFileDict(self.rootDir)
        if self.sortId == '':
            data = fileDict
            return data

        elif self.sortId == timeId:
            a = sortWithTime(fileDict)
            if self.selectCriteria == '':
                data = a.sort()
                return data
            else:
                data = sortTypeDecorator(a, self.selectCriteria).sort() or\
                       sortNameDecorator(a, self.selectCriteria).sort()
                return data

        elif self.sortId == nameId:
            a = sortWithName(fileDict)
            if self.selectCriteria == '':
                data = a.sort()
                return data
            else:
                return sortTypeDecorator(a, self.selectCriteria).sort() or\
                       sortNameDecorator(a, self.selectCriteria).sort()

        elif self.sortId == sizeId:
            a = sortWithSize(fileDict)
            if self.selectCriteria == '':
                data = a.sort()
                return data
            else:
                return sortTypeDecorator(a, self.selectCriteria).sort() or\
                       sortNameDecorator(a, self.selectCriteria).sort()


class chooseMode():
    def __init__(self, rootDir,  modeId):
        self.rootDir = rootDir
        self.modeId = modeId

    def choose(self):
        if self.modeId == logId:
            myFactory = logFactory()
            file = myFactory.createLogMode()
            myFactory = logFactory()
            file = myFactory.createLogMode()
            file.saveFile(self.rootDir)
            data = file.readFile(self.rootDir)

        elif self.modeId == compareId:
            mFactory = compareFactory()
            file = mFactory.createCompareMode()
            file.saveFile(self.rootDir)
            data = file.readFile(self.rootDir)
        return data


