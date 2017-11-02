#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import string,random
import re
import sys
import sys, time
import codecs
import sys   #引用sys模块进来，并不是进行sys的第一次加载
reload(sys)  #重新加载sys
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数import sys   #引用sys模块进来，并不是进行sys的第一次加载

data_path_output='/gfs/tts/wangzl/myBash/total_data/test'
def convert(outputf,num):
    num=str(num)
    lines=[line for line in codecs.open(outputf,'r','utf-8').readlines()]
    writer=codecs.open(outputf,'w','utf-8')
    writer.write(num+'\n')



    writer.writelines(lines)






if __name__=='__main__':
    #senten=u' 你好吗，我很好。'

    #senten.encode('unicode')
    num=100
    convert(data_path_output,num)
