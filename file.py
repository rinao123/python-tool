# -*- coding:utf-8 -*-
import os

def getPaths(rootDir, fileType = "*"):
    '''获取目录下所有指定类型文件的路径列表'''
    pathList = []
    for dirpath, dirnames, filenames in os.walk(rootDir):
        if len(filenames) > 0:
            for filename in filenames:
                extension = filename[filename.rfind(".") + 1:]
                if fileType == "*" or extension == fileType:
                    pathList.append(os.path.join(dirpath, filename))
    return pathList