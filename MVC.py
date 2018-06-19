from scanDir import *

class Model(object):
    def sortlogic(self, filepath, selectCriteria, sortId):
        filelist = getFileList(filepath)
        data = sortDir(filelist, selectCriteria, sortId).sort()
        return data

    def modelogic(self, filepath, modeId):
        data = chooseMode(filepath, modeId).choose()
        return data


class View(object):
    #排序中的data是一个只含完整文件名的列表
    def upsortdata(self,data):
        L = {}
        for file in data:
            p = File(file)
            L[file] = (p.file_name(), p.filetime(), p.filesize(), p.filetype())
        print('{:20s} {:24s} {:16s} {:10s}'.format('文件名', '修改时间', '文件大小', '文件类型'))
        for key, value in L.items():
            print('{:20s} {:30s} {:20s} {:10s}'.format(value[0], value[1], value[2], value[3]))
    #模式中的data是一个字典,可以直接输出
    def upmodedata(self, data):
        print('{:20s} {:24s} {:16s} {:10s}'.format('文件名', '修改时间', '文件大小', '文件类型'))
        for key, value in data.items():
            print('{:20s} {:30s} {:20s} {:10s}'.format(value[0], value[1], value[2], value[3]))


class Control(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def sortInterface(self, filepath, selectcriteria, sortId):
        data = self.model.sortlogic(filepath, selectcriteria, sortId)
        self.view.upsortdata(data)
    def modeInterface(self, filepath, modeId):
        data = self.model.modelogic(filepath, modeId)
        self.view.upmodedata(data)
#
if __name__ == '__main__':
    controller = Control()
    print("程序可以进入两种状态，排序和模式")
    print("排序中排序方式中输入数字1表示按照时间排序，输入数字2表示按照大小排序，输入数字3表示按照文件名排序")
    print("模式中模式方式中输入数字1表示日志模式，输入数字2表示差异模式")
    id = int(input("输入数字1进入排序，输入数字2进入模式："))
    if id == 1:
        filepath = input("输入文件路径：")
        selectcriteria = input("输入搜索关键字：")
        sortId = input("输入排序方式：")
        controller.sortInterface(filepath, selectcriteria, sortId)
    elif id == 2:
        filepath = input("请输入文件路径：")
        modeId = input("请输入模式方式：")
        controller.modeInterface(filepath, modeId)





