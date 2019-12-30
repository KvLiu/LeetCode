# -*- coding: utf-8 -*-
#https://www.nowcoder.com/practice/1b46eb4cf3fa49b9965ac3c2c1caf5ad?tpId=37&tqId=21285&tPage=4&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
#输入整数，计算二进制数中1的个数
while True:
    try:
        int1 = raw_input()
        bin_int= bin(int(int1))
        num=0
        for i in str(bin_int):
            if i == '1':
                num = num + 1
        print num
    except:
        break
