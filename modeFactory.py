from File import *
import pickle
class mode(object):
    def saveFile(self, rootDir):
        pass

    def readFile(self, rootDir):
        pass

class log(mode):
    def saveFile(self, rootDir):
        fileDict = getFileDict(rootDir)
        logName = pathToFileName(rootDir)
        with open(logName + '.pk', 'wb')as f:
                pickle.dump(fileDict, f)

    def readFile(self, rootDir):
        logName = pathToFileName(rootDir)
        with open(logName + '.pk', 'rb')as f:
            data = pickle.load(f)
        return data


class compare(mode):
    def saveFile(self, rootDir):

        compareDict = getFileDict(rootDir)
        logName = pathToFileName(rootDir)
        with open(logName + '.pk', 'rb')as f:
            logDict = pickle.load(f)

        logDictKey = set(logDict)
        compareDictKey = set(compareDict)

        removeFileKey = logDictKey - compareDictKey
        commonFileKey = logDictKey & compareDictKey
        addFileKey = compareDictKey - logDictKey

        data = {}
        for commonFile in commonFileKey:
            if compareDict[commonFile]['fileTime'] != logDict[commonFile]['fileTime']:
                data[commonFile] = {'fileTime': compareDict[commonFile]['fileTime'],
                                 'fileSize': compareDict[commonFile]['fileSize'],
                                 'fileType': compareDict[commonFile]['fileType'],
                                'fileName': commonFile + '  修改的文件'}


        for removeFile in removeFileKey :
            data[removeFile] = {'fileTime': logDict[removeFile]['fileTime'],
                                'fileSize': logDict[removeFile]['fileSize'],
                          'fileType': logDict[removeFile]['fileType'], 'fileName': removeFile + '  删除的文件'}
        for addFile in addFileKey:
            data[addFile] = {'fileTime': compareDict[addFile]['fileTime'],
                             'fileSize': compareDict[addFile]['fileSize'],
                          'fileType': compareDict[addFile]['fileType'], 'fileName': addFile + '  新增的文件'}

        return data

    def readFile(self, rootDir):
        data = self.saveFile(rootDir)
        return data


class modeFactory(object):
    def createMode(self):
        pass


class logFactory(modeFactory):
    def createLogMode(self):
        return log()


class compareFactory(modeFactory):
    def createCompareMode(self):
        return compare()
