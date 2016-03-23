#-*-coding:utf-8-*-
'''
Created on 2014年11月24日

@author: baihe
'''
from sklearn.externals import joblib
import sys
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
import process_tool

reload(sys)
# sys.setdefaultencoding("utf-8")
n_top_words = 50
n_features = 10000

#从文件导入停用词表
stpwrdlst = process_tool.read_stopword("extra_dict/stop_words.txt")

vectorizer = TfidfVectorizer(max_df=0.7, min_df=5, max_features=n_features,stop_words=stpwrdlst)
#load train_set
train_set = joblib.load("wordbag/train_set1124.data")

clusters = len(train_set.target_name)

print "共",clusters,"种类别:",train_set.target_name

for i in range(0,clusters):
        findx = train_set.label.index(i)
        counts = train_set.label.count(i)
        lindx = findx+counts-1
        
        vectorizer = TfidfVectorizer(max_df=0.8, min_df=2, max_features=n_features,
                             stop_words=stpwrdlst)
        tfidf = vectorizer.fit_transform(train_set.contents[findx:lindx])
        # Fit the NMF model
        nmf = NMF(n_components=1, random_state=1).fit(tfidf)
        
        feature_names = vectorizer.get_feature_names()
        
        # print "nmf.components_:",len(nmf.components_)
        print("Topic :",train_set.target_name[i])
        print 'nmf.components_:',nmf.components_.shape
        print(" ".join([feature_names[i]
                    for i in nmf.components_[0].argsort()[:-n_top_words - 1:-1]]))