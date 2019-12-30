"""
试题字母计数法
在某种场景下，开发人员决定使用字母来表示一个正整数，该方法利用英文的小写字母表示，映射规则很简单，按字母顺序每一个字母都代表一个值。如下所示列表中的部分内容。
字母表示 对应十进制
a 1
b 2
...
z 26
aa 27
ab 28
...
huawei 104680767
"""
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
list2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    sum =0
    string = raw_input()
    for i in xrange(0,len(string),1):
        #print string[i]
        index = list2.index(string[i])
        #print 'index=',index
        #print 'list1[index]=',list1[index]
        #sum = sum + list1[index]*pow(26,len(string)-i-1)
        sum =sum + (index+1)*pow(26,len(string)-i-1)
    print sum
