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

corpus_path = "corpus"+"/"
token_path = "token"+"/"

dir_list = os.listdir(corpus_path)

for file in dir_list:
    file_name = corpus_path+file
    file_read = open(file_name,"r")
    
    token_file = token_path + file
    file_write = open(token_file,'a')
    
    for line in file_read:
        temp = line.strip()
        seg_corpus = jieba.cut(temp)
        file_write.write(" ".join(seg_corpus)+"\n")
    
    file_read.close()
    file_write.close()
print "分词成功！！！！"
   

