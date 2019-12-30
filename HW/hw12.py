# -*- coding:utf-8 -*-
#求正整数质数因子
#reference: https://www.nowcoder.com/profile/9429149/codeBookDetail?submissionId=12633593
while True:
    try:
        n = raw_input()
        if not isinstance(eval(n),int):
            exit(-1)
        n = int(n)
        res=""
        for i in range(2,n+1):
            while n%i==0:
                res = res+ str(i)+" "
                n=n/i
        print res
    except:
        break
