# -*- coding: utf-8 -*-
'''
Created on 2014年11月21日

@author: baihe
'''
import sys
import os
import datetime

from sklearn.datasets.base import Bunch
from sklearn.externals import joblib

from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

reload(sys)
sys.setdefaultencoding('utf-8')

#导入训练集
train_path = "wordbag" + "/" + "train_set1124.data"
data_set = joblib.load(train_path)
# print data_set.target_name
# print data_set.contents[0]
####exit
# sys.exit(0)
#定义词袋数据结构
#tf-idf计算后的词袋
wordbag = Bunch(target_name=[],label=[],filenames=[],tdm=[],vocabulary={})
wordbag.target_name = data_set.target_name
wordbag.label = data_set.label
#语料
corpus = data_set.contents

#导入停用词
stopwordpath = "extra_dict/stop_words.txt"
stopword_dic = open(stopwordpath,'r')
stopword_content = stopword_dic.read()
#将停用词转为list
stopwordlist = stopword_content.splitlines()
stopword_dic.close()

#词袋创建时间
start = datetime.datetime.now()
print start
#使用 TfidfVectorizer创建词袋
vectorize = TfidfVectorizer(sublinear_tf=True,max_df = 0.8,min_df=3,max_features=50000,stop_words=stopwordlist)

feature_train = vectorize.fit_transform(corpus)

#计算词袋结束时间
end = datetime.datetime.now()
print 'create word bag peroid:',(end - start).seconds,"seconds"

#计算词袋的行列数
print 'Size of fea_train:\n',feature_train.shape

wordbag.tdm = feature_train
wordbag.vocabulary = vectorize.vocabulary_
# print wordbag.vocabulary
# print wordbag.tdm[0:5]
#持久化
joblib.dump(wordbag,"wordbag/word_bag1124.data",compress=9)
word_bag1124 = joblib.load("wordbag/word_bag1124.data")
print word_bag1124.target_name