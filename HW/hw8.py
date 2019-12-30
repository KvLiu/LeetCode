# -*- coding: utf-8 -*-
#两个字符串的最大公共字串的长度，字符不区分大小写
#https://www.nowcoder.com/profile/6880157/codeBookDetail?submissionId=11572880
def compare(s1,s2):
    res= 0
    #生成0矩阵，为方便后续计算，比字符串长度多了一列
    m = [[0 for i in xrange(0,len(s2)+1)] for j in xrange(0,len(s1)+1)]
    for i in xrange(0,len(s1)):
        for j in xrange(0,len(s2)):
            if s1[i]==s2[j]:
                m[i+1][j+1] = m[i][j]+1
                if m[i+1][j+1] >res:
                    res=m[i+1][j+1]
    return res

while True:
    try:
        s1= raw_input().lower()
        s2= raw_input().lower()
        print compare(s1,s2)
    except:
        break
