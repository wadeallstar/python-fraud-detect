#-*-coding:utf-8-*-
import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

# USAGE = "usage:    python extract_tags_stop_words.py [file name] -k [top k]"
# 
# parser = OptionParser(USAGE)
# parser.add_option("-k", dest="topK")
# opt, args = parser.parse_args()
# 
# 
# if len(args) < 1:
#     print USAGE
#     sys.exit(1)
# 
# file_name = args[0]
# 
# if opt.topK is None:
#     topK = 10
# else:
#     topK = int(opt.topK)

# content = open(file_name, 'rb').read()
content="你好的了，欢迎访问北京大学,北京大学"

jieba.analyse.set_stop_words("../extra_dict/stop_words.txt")
# jieba.analyse.set_idf_path("../extra_dict/idf.txt.big");

tags = jieba.analyse.extract_tags(content)

print " ".join(tags)
