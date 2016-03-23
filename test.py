#-*-coding:utf-8-*-

'''
Created on 2014年11月20日

@author: baihe
'''
import jieba
import re
import jieba.posseg as pseg

temp = "我的，你的了,你好，hello"
temp = temp.decode("utf8")

string = re.sub("[\s+\.+\!+\/+_+,+$+%+\*\+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"),temp)

stopFile = open('extra_dict/stop_words.txt','r')
stopWord = [line.strip().decode('utf-8') for line in stopFile]
# print set(stopWord)
print string
fenci=jieba.cut(string,cut_all=False)

# pos = pseg.cut(string)
# for w in pos:
#     print w.word,w.flag

words = " ".join(list(set(fenci)-set(stopWord)))
for w in words.split(' '):
    print w
print words

