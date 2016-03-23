#-*-coding:utf-8-*-
'''
Created on 2014年11月21日

@author: baihe
'''
import sys
import os
import jieba
from sklearn.datasets.base import Bunch
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

'''
srcdir:源文件存放目录
dstdir：目的文件存放目录
'''
def chinesefenci(srcdir,dstdir):
    dir_list = os.listdir(srcdir)

    for file in dir_list:
        file_name = srcdir+"/"+file
        file_read = open(file_name,"r")
        
        token_file = dstdir +"/"+ file
        file_write = open(token_file,'a')
        
        for line in file_read:
            temp = line.strip()
            seg_corpus = jieba.cut(temp)
            file_write.write(" ".join(seg_corpus)+"\n")
        
        file_read.close()
        file_write.close()
    print "分词成功！！！！"
'''
token_path:分词后的文件存放目录
wordbag_path：词袋存放位置
'''
def train_bags(token_path,filename,wordbag_path):
    data_set = Bunch(tatget_name=[],label=[],filenames=[],contents=[])

    dir_list = os.listdir(token_path)
    data_set.target_name = dir_list
    
    for file in dir_list:
        file_name = token_path+"/"+file
        file_read = open(file_name,"r")
        for line in file_read:
            data_set.label.append(data_set.target_name.index(file))
            data_set.contents.append(line.strip())
        file_read.close()
    #持久化
    joblib.dump(data_set, wordbag_path+"/"+filename, compress=3)
'''
stopwordfile:停用词存放目录
'''
def read_stopword(stopwordfile):
    stopword_dic = open(stopwordfile,'r')
    stopword_content = stopword_dic.read()
    #将停用词转为list
    stopwordlist = stopword_content.splitlines()
    stopword_dic.close()
    return stopwordlist
'''
trainsetfile:train_set.data
stopwordfile:停用词路径
dstdir：存放路径
'''
def calc_tfidf(trainsetfile,stopwordfile,dstdir):
    data_set = joblib.load(trainsetfile)
    wordbag = Bunch(target_name=[],label=[],filenames=[],tdm=[],vocabulary={})
    wordbag.target_name = data_set.tatget_name
    wordbag.label = data_set.label
    
    corpus = data_set.contents
    stopwordlist = read_stopword(stopwordfile)
    vectorize = TfidfVectorizer(sublinear_tf=True,max_df = 0.8,min_df=3,max_features=50000,stop_words=stopwordlist)
    feature_train = vectorize.fit_transform(corpus)
    wordbag.tdm = feature_train
    wordbag.vocabulary = vectorize.vocabulary_
    joblib.dump(wordbag,dstdir+"/"+"word_bag.data",compress=3)
'''
testsetfile:test_set.data
stopwordfile:停用词路径
dstdir：存放路径
myvocabulary:trainset‘s vocabulary
'''
def testset_tfidf(testsetfile,stopwordfile,myvocabulary):
    data_set = joblib.load(testsetfile)
    wordbag = Bunch(target_name=[],label=[],filenames=[],tdm=[],vocabulary={})
    wordbag.target_name = data_set.tatget_name
    wordbag.label = data_set.label
    
    corpus = data_set.contents
    stopwordlist = read_stopword(stopwordfile)
    vectorize = TfidfVectorizer(sublinear_tf=True,stop_words=stopwordlist,vocabulary=myvocabulary)
    feature_train = vectorize.fit_transform(corpus)
    wordbag.tdm = feature_train
    joblib.dump(wordbag,"test_wordbag/test_word_bag.data",compress=3)
    return wordbag
    