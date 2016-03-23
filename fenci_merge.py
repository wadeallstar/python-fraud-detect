#-*-coding:utf-8-*-
'''
Created on 2014年11月21日

@author: baihe
'''
import sys
import os
import jieba

reload(sys)
# sys.setdefaultencoding('utf-8')

corpus_path = "ChineseWord"+"/"
token_path = "SouGouWordSegmention"+"/"

dir_list = os.listdir(corpus_path)

print dir_list
for dir in dir_list:
    dir_name = corpus_path+dir
    file_list = os.listdir(dir_name)
    if not os.path.exists(token_path+dir):
        os.mkdir(token_path+dir)
    for file in file_list:
        file_name = dir_name+"/"+file
        file_write = open(token_path+dir+"/"+file,'w')
        file_read = open(file_name,"r")
        for line in file_read:
            temp = line.strip()
            seg_corpus = jieba.cut(temp)
            file_write.write(" ".join(seg_corpus)+"\n")
        file_read.close()
        file_write.close()
print "分词成功！！！！"
    

