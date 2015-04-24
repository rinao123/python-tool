# -*- coding:utf-8 -*-
import file
import os

if __name__ == '__main__':
    pathList = file.getPaths(r"E:\xml")
    for path in pathList:
        f = open(path)
        while True:
            line = f.readline()
            if not line:
                break
            if "灵剑" in line:
                print path, line
    