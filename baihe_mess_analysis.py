#-*-coding:utf-8-*-

'''
Created on 2014年11月20日

@author: baihe
'''
import jieba
import re
import jieba.posseg as pseg

temp = "你好，刚刚看了你的资料觉得蛮合适的，我在校是学舞蹈类的，你想了解我的话加我的Q 979 036 600"
temp = temp.decode("utf8")
string = re.sub("[qQ]".decode("utf8"), "qq".decode("utf8"), temp)
string = re.sub("[\s+\.+\!+\/+_+,+$+%+\*\+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"),string)

print string
fenci=jieba.cut(string,cut_all=False)


pos = pseg.cut(string)
for w in pos:
    if(w.flag=="qq"):       
        print w.word,w.flag
        break
words = " ".join(fenci)
print words