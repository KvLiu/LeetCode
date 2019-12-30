# -*- coding:utf-8 -*-
#输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
#Reference: https://www.nowcoder.com/profile/777916/codeBookDetail?submissionId=4180395
while True:
    try:
        n = raw_input()
        if not isinstance(eval(n),int):
            break

        n = n[::-1]
        res=""
        for i in str(n):
            if i not in res:
                res=res+str(i)
        print res
    except:
        break
