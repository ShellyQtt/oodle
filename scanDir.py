from sortStrategy import *
from sortDecorator import *
from modeFactory import *
timeId = '1'
sizeId = '2'
nameId = '3'
logId = '1'
compareId = '2'

class sortDir():
    def __init__(self, filelist, selectCriteria, sortId):
        self.filelist = filelist
        self.selectCriteria = selectCriteria
        self.sortId = sortId

    def sort(self):
        if self.sortId == '':
            filelist = self.filelist
            self.save(filelist)
            return filelist

        elif self.sortId == timeId:
            filelist = sortWithTime(self.filelist).sort()
            if self.selectCriteria == '':
                self.save(filelist)
                return filelist
            else:
                filelist = sortTypeDecorator(filelist, self.selectCriteria).sort() or\
                       sortNameDecorator(filelist, self.selectCriteria).sort()
                # self.save(filelist)
                return filelist

        elif self.sortId == nameId:
            filelist = sortWithName(self.filelist).sort()
            if self.selectCriteria == '':
                self.save(filelist)
                return filelist
            else:
                return sortTypeDecorator(filelist, self.selectCriteria).sort() or\
                       sortNameDecorator(filelist, self.selectCriteria).sort()

        elif self.sortId == sizeId:
            filelist = sortWithSize(self.filelist).sort()
            if self.selectCriteria == '':
                self.save(filelist)
                return filelist
            else:
                return sortTypeDecorator(filelist, self.selectCriteria).sort() or\
                       sortNameDecorator(filelist, self.selectCriteria).sort()

    def save(self, filelist):
        myFactory = logFactory()
        file = myFactory.createLogMode()
        file.saveFile(filelist)

class chooseMode():
    def __init__(self, filepath,  modeId):
        self.filepath = filepath
        self.modeId = modeId

    def choose(self):
        if self.modeId == logId:
            myFactory = logFactory()
            file = myFactory.createLogMode()
            data = file.readFile(self.filepath)
        elif self.modeId == compareId:
            filename = getFileList(self.filepath)
            mFactory = compareFactory()
            file = mFactory.createCompareMode()
            file.saveFile(filename)
            data = file.readFile(filename)
        return data
