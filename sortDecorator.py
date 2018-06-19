from sortStrategy import  *
from File import *
class sortCriteriaDecorator(sortFile):
    def sort(self):
        pass

class sortNameDecorator(sortCriteriaDecorator):
    def __init__(self, sortfile, name):#传入的sortfile是一个排序后文件列表
        self.sortfile = sortfile
        self.name = name

    def sort(self):
        L = {}
        list = []
        for file in self.sortfile:
            p = File(file)
            # print(p.file_name())
            if self.name in p.file_name():
                list.append(file)
        return list

class sortTypeDecorator(sortCriteriaDecorator):
    def __init__(self, sortfile, type):
        self.sortfile = sortfile
        self.type = type

    def sort(self):
        L = {}
        list = []
        for file in self.sortfile:
            p = File(file)
            if self.type == p.filetype():
                list.append(file)
        return list

# filename = getFileList("D://学习")
# p = sortWithName(filename)
# a = sortTypeDecorator(sortWithName(filename).sort(), ".txt")
# list = a.sort()
# print(list)