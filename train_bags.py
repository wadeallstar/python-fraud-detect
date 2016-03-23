#-*-coding:utf-8-*-
'''
Created on 2014年11月21日

@author: baihe
'''
import sys
import os

from sklearn.datasets.base import Bunch

from sklearn.externals import joblib
import jieba
from sklearn.feature_extraction.text import HashingVectorizer

reload(sys)
# sys.setdefaultencoding('utf-8')

token_path = "token"+"/"
#次袋语料路径
wordbag_path = "wordbag"+"/"
#是引用bunch存储
data_set = Bunch(target_name=[],label=[],filenames=[],contents=[])

dir_list = os.listdir(token_path)
data_set.target_name = dir_list

for file in dir_list:
    file_name = token_path+file
    file_read = open(file_name,"r")
    for line in file_read:
        data_set.label.append(data_set.target_name.index(file))
        data_set.contents.append(line.strip())
    file_read.close()
#持久化
joblib.dump(data_set, wordbag_path+"train_set1124.data", compress=3)

#验证
data_set = joblib.load(wordbag_path+"train_set1124.data")
print data_set.target_name

# print data_set.label
# 
# print len(data_set.contents)

