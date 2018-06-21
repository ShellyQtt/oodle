import sys

from scanDir import *

class Model(object):
    def sortlogic(self, rootDir, selectCriteria, sortId):
        data = sortDir(rootDir, selectCriteria, sortId).sort()
        return data

    def modelogic(self, rootDir, modeId):
        data = chooseMode(rootDir, modeId).choose()
        return data

class View(object):

    def updata(self, data):
        print('{:25s} {:10s} {:10s} {:30s}'.format('修改时间', '文件大小', '文件类型','文件名'))
        for key, value in data.items():
            print('{:30s} {:13s} {:13s} {:30s}'.format(value['fileTime'], value['fileSize']
                                                       , value['fileType'], value['fileName']))

class Control(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def sortInterface(self, rootDir, selectCriteria, sortId):
        data = self.model.sortlogic(rootDir, selectCriteria, sortId)
        self.view.updata(data)

    def modeInterface(self, rootDir, modeId):
        data = self.model.modelogic(rootDir, modeId)
        self.view.updata(data)
#
if __name__ == '__main__':
    controller = Control()
    print("程序可以进入两种状态，排序和模式")
    print("排序中排序方式中输入数字1表示按照时间排序，输入数字2表示按照大小排序，输入数字3表示按照文件名排序")
    print("模式中模式方式中输入数字1表示日志模式，输入数字2表示差异模式")
    id = int(input("输入数字1进入排序，输入数字2进入模式："))
    if id == 1:
        rootDir = input("输入文件路径：")
        if not os.path.exists(rootDir):
            print("输入的路径名有误")
            sys.exit()
        selectCriteria = input("输入搜索关键字：")
        sortId = input("输入排序方式：")
        controller.sortInterface(rootDir, selectCriteria, sortId)
    elif id == 2:
        rootDir = input("请输入文件路径：")
        modeId = input("请输入模式方式：")
        controller.modeInterface(rootDir, modeId)





