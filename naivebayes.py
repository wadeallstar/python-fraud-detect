
# -*- coding: utf-8 -*-
import re
import sys
import jieba
import warnings
from sklearn.externals import joblib
from sklearn.naive_bayes import MultinomialNB
import process_tool
from sklearn.feature_extraction.text import TfidfVectorizer 
# 配置utf-8输出环境
reload(sys)
# sys.setdefaultencoding('utf-8')

#从文件导入停用词表
stpwrdlst = process_tool.read_stopword("extra_dict/stop_words.txt")
# testsamp = TextPreprocess()
# 导入训练词袋模型
train_set = joblib.load("wordbag/word_bag1124.data")
# clf = MultinomialNB(alpha = 0.001).fit(train_set.tdm, train_set.label)
# joblib.dump(clf,"model/MultinomialNB.model",compress=3)
clf = joblib.load("model/MultinomialNB.model")
# clf = joblib.load("model/MultinomialNB.model")
a = 1
while a:
    # 导入测试语料
    print "please input chinese words(input stop proceduce will break):"
    words = sys.stdin.readline()
    words = words.decode("utf8")
    words = re.sub("[\s\.\!\/_,\$%\*\+\"\'\\\]+|[+——！，。？、~@#￥%……&*（）‘’“”]+".decode("utf8"), "".decode("utf8"),words)
    print words
    if(words.strip()=="stop"):
        a = 0
    else:
        test_data = []
        fenci = jieba.cut(words)
        result = " ".join(fenci)
        print result
        test_data.append(result)
#         print test_data
        
        vectorizer = TfidfVectorizer(sublinear_tf = True,max_df = 0.5,stop_words=stpwrdlst,vocabulary=train_set.vocabulary)
        fea_test = vectorizer.fit_transform(test_data)

        predicted = clf.predict(fea_test)
        if predicted==0:
            label = "fraud"
        else:
            label = "normal"
        print "preidct label:",label
        print "\n"
        
print "procedure exited!!!!"
