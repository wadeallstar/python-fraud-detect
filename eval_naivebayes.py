# -*- coding: utf-8 -*-
'''
Created on 2014年11月21日

@author: baihe
'''
import numpy as np
import sys
import jieba
import warnings
from sklearn.externals import joblib
from sklearn.naive_bayes import MultinomialNB
import process_tool
from sklearn.metrics.metrics import classification_report
from sklearn.metrics import confusion_matrix
np.set_printoptions(threshold=np.nan)
# 配置utf-8输出环境
reload(sys)
sys.setdefaultencoding('utf-8')
#从文件导入停用词表
stpwrdlst = process_tool.read_stopword("extra_dict/stop_words.txt")
#训练集读取
train_set = joblib.load("wordbag/word_bag1124.data")
print train_set.target_name
# print "fenci"
# process_tool.chinesefenci("test_corpus", "test_token")
# print "train_bag"
# process_tool.train_bags("test_token","test_set.data", "test_wordbag")
# print "test tfidf"
# test_data = process_tool.testset_tfidf("test_wordbag/test_set.data", "extra_dict/stop_words.txt", train_set.vocabulary)
test_data = joblib.load("test_wordbag/test_word_bag.data")
# print "MultinomialNB train"
# clf = MultinomialNB(alpha = 0.001).fit(train_set.tdm, train_set.label)
# joblib.dump(clf,"model/MultinomialNB.model",compress=3)

clf = joblib.load("model/MultinomialNB.model")
print (test_data.tdm).shape
print len(test_data.label)

# print clf.predict(test_data.tdm)
print test_data.target_name
print classification_report(np.array(test_data.label), clf.predict(test_data.tdm),target_names=train_set.target_name)

cm = confusion_matrix(np.array(test_data.label), clf.predict(test_data.tdm))
print cm
