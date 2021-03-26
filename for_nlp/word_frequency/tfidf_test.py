# coding:utf-8

import jieba
import jieba.posseg as pseg
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == "__main__":
    # corpus=["我 来到 北京 清华大学",#第一类文本切词后的结果，词之间以空格隔开
    # "他 来到 了 网易 杭研 大厦", #第二类文本的切词结果
    # "小明 硕士 毕业 与 中国 科学院",#第三类文本的切词结果
    # "我 爱 北京 天安门"] #第四类文本的切词结果
    vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer.vocabulary = ['交通事故']
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
    # frequency_matrix = vectorizer.fit_transform(corpus)
    frequency_matrix = [[0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 55, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 15529, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 4766, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
                        [0, 0, 0, 0, 0, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    tfidf = transformer.fit_transform(frequency_matrix)  # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    # print(vectorizer.get_feature_names())
    # print(frequency_matrix.toarray())
    # word=vectorizer.get_feature_names()#获取词袋模型中的所有词语
    word = ['离退休人员返聘合同纠纷', '请求确认人民调解协议效力', '劳动合同纠纷', '社会保险纠纷', '福利待遇纠纷', '劳动合同纠纷', '社会保险纠纷', '侵害商业秘密纠纷']
    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    print(weight)
    for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
        print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
        for j in range(len(word)):
            print(word[j], weight[i][j])
