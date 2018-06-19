import os
from File import *

class sortFile(object):
    def sort(self):
        pass

class sortWithName(sortFile):
    def __init__(self,filelist):
        self.filelist = filelist

    def sort(self):
        L = {}
        list = []
        for file in self.filelist:
            p = File(file)
            L[file] = p.file_name()
        k = sorted(L.items(), key=lambda L: L[1], reverse=True)
        for i in range(len(k)):
            list.append(k[i][0])
        return list



class sortWithTime(sortFile):
    def __init__(self,filelist):
        self.filelist = filelist

    def sort(self):
        L = {}
        list = []
        for file in self.filelist:
            p = File(file)
            L[file] = p.filetime()
        k = sorted(L.items(), key=lambda L: L[1], reverse=True)
        for i in range(len(k)):
            list.append(k[i][0])
        return list


class sortWithSize(sortFile):
    def __init__(self,filelist):
        self.filelist = filelist

    def sort(self):
        L = {}
        list = []
        for file in self.filelist:
            p = File(file)
            L[file] = p.filesize()
        k = sorted(L.items(), key=lambda L: L[1], reverse=True)
        for i in range(len(k)):
            list.append(k[i][0])
        return list

# filename = getFileList("D://学习")
# print(sortWithName(filename).sort())

