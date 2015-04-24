# -*- coding:utf-8 -*-
def isStringLike(obj):
    '''判断一个对象是否类字符串'''
    try:
        obj + ''
        return True
    except:
        return False
    
def getExtention(filename):
    '''获取文件名的后缀'''
    return filename[filename.rfind(".") + 1:]