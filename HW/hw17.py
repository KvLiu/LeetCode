# -*- coding: utf-8 -*-
#开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，
#从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
#输入：
#合法坐标为A(或者D或者W或者S) + 数字（两位以内）
#坐标之间以;分隔。
#非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
#下面是一个简单的例子 如：
#A10;S20;W10;D30;X;A1A;B10A11;;A10;
while True:
    try:
        m=n=0
        str_li = raw_input().split(';')
        for s in str_li:
            if len(s)<2 or len(s)>3:
                pass
            else:
                #判断S是否以A开头并且S[1:]是否为数字
                if s.startswith('A') and s[1:].isdigit():
                    m= m-eval(s[1:])
                elif  s.startswith('D') and s[1:].isdigit():
                    m= m+eval(s[1:])
                elif  s.startswith('W') and s[1:].isdigit():
                    n= n+eval(s[1:])
                elif  s.startswith('S') and s[1:].isdigit():
                    n= n-eval(s[1:])

        print str(m)+','+str(n)

    except:
        break
