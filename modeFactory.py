# from scanDir import *
from File import *
import pickle
class mode(object):
    def saveFile(self, filelist):
        pass
    def readFile(self, filepath):
        pass


class log(mode):
    def saveFile(self, filelist):#filelist是该路径下进行的排序的
        # L = printFile(filelist)
        L = {}
        for file in filelist:
            p = File(file)
            L[file] = (p.file_name(), p.filetime(), p.filesize(), p.filetype())
        a = File(filelist[0])
        filepath = a.filepath()
        str = pathToFilename(filepath)
        with open(str + '.pk', 'wb')as f:
                pickle.dump(L, f)

    def readFile(self, filepath):
        str = pathToFilename(filepath)
        with open(str + '.pk', 'rb')as f:
            data = pickle.load(f)
        return data


class compare(mode):
    def saveFile(self, filelist):
        K = {}
        a = File(filelist[0])
        filepath = a.filepath()
        comparelist = getFileList(filepath)
        # K = printFile(comparelist)
        for file in comparelist:
            p = File(file)
            K[file] = (p.file_name(), p.filetime(), p.filesize(), p.filetype())
        str = pathToFilename(filepath)
        with open(str + '.pk', 'rb')as f:
            L = pickle.load(f)
        data = {}
        c = list(L.keys() - K.keys()) + list(K.keys() - L.keys())
        for key, value in (L.items() - K.items()):
            data[key] = value
        for key, value in (K.items() - L.items()):
            data[key] = value
        for key, value in data.items():
            if key in list(K.keys() - L.keys()):
                a = File(key)
                data[key] = (a.file_name(),'','','')
            elif key in list(L.keys() - K.keys()):
                data[key] = (key,'','','')

        return data

    def readFile(self, filelist):
        data = self.saveFile(filelist)
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
