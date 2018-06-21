import datetime
import os
class File(object):

    def __init__(self, fileName):
        super().__init__()
        self.fileName = fileName

    def filename(self):
        (filePath, tempFileName) = os.path.split(self.fileName)
        return (tempFileName)

    def fileTime(self):
        mTime = os.path.getmtime(self.fileName)
        date = datetime.datetime.fromtimestamp(mTime)
        return (date.strftime('%Y-%m-%d %H:%M:%S'))

    def fileSize(self):
        if (os.path.isfile(self.fileName)):
            size = os.stat(self.fileName).st_size
            sizeName = str(round(size / 1024)) + 'KB'
        else:
            fileList = os.listdir(self.fileName)
            size = 0
            for file in fileList:
                fullPath = os.path.join(self.fileName, file)
                size += os.stat(fullPath).st_size
            sizeName = str(round(size / 1024)) + 'KB'
        return (sizeName)


    def fileType(self):
        if (os.path.isfile(self.fileName)):
            (filePath, tempFileName) = os.path.split(self.fileName)
            (shotName, extension) = os.path.splitext(tempFileName)
            return (extension)
        else:
            return (" Dir")

    def filePath(self):
        (filePath, tempFileName) = os.path.split(self.fileName)
        return (filePath)

def getFileDict(rootDir):
    fileDict = {}
    fileList = os.listdir(rootDir)
    for file in fileList:
        fullPath = os.path.join(rootDir, file)
        a = File(fullPath)
        fileDict[file] = {'fileTime': a.fileTime(), 'fileSize': a.fileSize(), 'fileType': a.fileType(), 'fileName': a.filename()}
    return fileDict

def pathToFileName(path):
    return path.replace("\\", "")\
        .replace(":", "")\
        .replace("/", "")
#


# L = {'qtt':{'ab':'1KB','bc':2},'wbh':{'ab':'2KB','cd':1}}
# for key, value in L.items():
#     print(value['ab'])
# # k = set(L)
# # print(k)
# # L.pop('lxr')
# for key in L:
#     print(key)
#
# print(dict(sorted(L.items(), key=lambda x:x[1]['ab'][:-2])))

# K = {'qtt':'cb','wbh':'bc','lh':'cd'}
# a = L.keys[) - K.keys()
# b = K.items() - L.items()
