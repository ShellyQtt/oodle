import datetime
import math
import os
class File(object):
    def __init__(self,filename):
        self.filename = filename
    def file_name(self):
        return getFileName(self.filename)
    def filetime(self):
        return getFileTime(self.filename)
    def filesize(self):
        return getFileSize(self.filename)
    def filetype(self):
        return getFileType(self.filename)
    def filepath(self):
        return getFilePath(self.filename)

# def printFile(filelist):
#     L = {}
#     for file in filelist:
#         p = File(file)
#         L[file] = (p.file_name(), p.filetime(), p.filesize(), p.filetype())
#     print('{:20s} {:24s} {:16s} {:10s}'.format('文件名', '修改时间', '文件大小', '文件类型'))
#     for key, value in L.items():
#         print('{:20s} {:30s} {:20s} {:10s}'.format(value[0], value[1], value[2], value[3]))

def getFileTime(filename):
    mtime = os.path.getmtime(filename)
    date = datetime.datetime.fromtimestamp(mtime)
    return (date.strftime('%Y-%m-%d %H:%M:%S'))

def getFileSize(filename):
    if (os.path.isfile(filename)):
        size = os.stat(filename).st_size
        sizename = str(round(size / 1024)) + 'KB'
    else:
        filelist = os.listdir(filename)
        size = 0
        for file in filelist:
            fullpath = os.path.join(filename, file)
            size += os.stat(fullpath).st_size
        sizename = str(round(size / 1024)) + 'KB'
    return (sizename)

def getFileName(filename):
    (filepath, tempfilename) = os.path.split(filename)
    return (tempfilename)

def getFileType(filename):
    if(os.path.isfile(filename)):
        (filepath, tempfilename) = os.path.split(filename)
        (shotname, extension) = os.path.splitext(tempfilename)
        return (extension)
    else:
        return("文件夹")

def getFileList(rootdir):
    filelist = []
    filenames = os.listdir(rootdir)
    for filename in filenames:
        file = os.path.join(rootdir, filename)
        filelist.append(file)
    return filelist  #filist 是一个包括路径的文件名的列表

def pathToFilename(str):
    s = str.replace('/', '')
    a = s.replace(':', '')
    return a
# p = getFileList("D://学习")
# L = {}
# for file in p:
#     p = File(file)
#     L[file] = p.file_name()
# k = sorted(L.items(), key=lambda L: L[1], reverse=True)
# print()
# print(p)

def getFilePath(filename):
    (filepath, tempfilename) = os.path.split(filename)
    return (filepath)

# filelist = getFileList("D://学习")
# data = printFile(filelist)
# print('{:20s} {:24s} {:16s} {:10s}'.format('文件名','修改时间', '文件大小','文件类型'))
# for key,value in data.items():
#     print('{:20s} {:30s} {:20s} {:10s}'.format(value[0],value[1],value[2],value[3]))
#
# p = File("D://学习/星期五")
# print(p.filesize())#返回的文件名等都是字符串类型的，给定的路径是文件夹的话后缀名为文件夹，大小不显示