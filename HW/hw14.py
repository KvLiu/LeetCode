#编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。不在范围内的不作统计。
#Reference: https://www.nowcoder.com/profile/7399104/codeBookDetail?submissionId=12709974
#Solution 1: string convert to set
while True:
    try:
        def sta_char(s):
            s=list(set(list(s)))
            length=0
            for i in s:
                if ord(i)<128 and ord(i)>=0:
                    length+=1
            return length
        string=raw_input()
        print sta_char(string)
    except:
        break
#Solution2: string convert to list
def strlen(s):
    l =list(s)
    newl =[]
    for i in l:
        if ord(i)>= 0 and ord(i)<=128 and i not in newl:
            newl.append(i)
    return len(newl)
while True:
    try:
        n = raw_input()
        print strlen(n)
    except:
        break
