# -*- coding: utf-8 -*-
import sys
"""题目描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。
所有的IP地址划分为 A,B,C,D,E五类
A类地址1.0.0.0~126.255.255.255; B类地址128.0.0.0~191.255.255.255;
C类地址192.0.0.0~223.255.255.255; D类地址224.0.0.0~239.255.255.255；
E类地址240.0.0.0~255.255.255.255
私网IP范围是：
10.0.0.0～10.255.255.255
172.16.0.0～172.31.255.255
192.168.0.0～192.168.255.255
子网掩码为前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
本题暂时默认以0开头的IP地址是合法的，比如0.1.1.2，是合法地址
输入描述:
多行字符串。每行一个IP地址和掩码，用~隔开。
输出描述:
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。
示例1
输入
10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0
输出
1 0 1 0 0 2 1
"""
A=B=C=D=E=err=pri=0
mask_num=['254','252','248','240','224','192','128','0']
def chk_iP(ip):
    ip = ip.split('.')
    if len(ip) !=4:
        return 0
    for i in ip:
        if not i.isdigit() or not 0<=int(i)<=255:
            return 0
    return 1

def chk_mask(mask):
    mask = mask.split('.')
    if len(mask) !=4:
        return 0
    if int(mask[0])==255:
        if int(mask[1]) ==255:
            if int(mask[2]) ==255:
                if mask[3] in mask_num:
                    return 1
                else:
                    return 0
            elif mask[2] in mask_num and mask[3]=='0':
                return 1
            else:
                return 0
        elif mask[1] in mask_num and mask[2]=='0' and mask[3] =='0':
            return 1
        else:
            return 0
    elif mask[0] in mask_num and mask[1]=='0' and mask[2]=='0' and mask[3] =='0':
        return 0
    else:
        return 1

while True:
    try:
        #ip_str= sys.stdin.readline().split('~')
        ip_str = raw_input().split('~')
        if len(ip_str)!=2:
            break
        ip = ip_str[0]
        mask = ip_str[1]
        if chk_iP(ip) and chk_mask(mask):
            ip=ip.split('.')
            mask = mask.split('.')
            if 1<=int(ip[0])<=126:
                A= A+1
            if 128<=int(ip[0])<=191:
                B=B+1
            if 192<=int(ip[0])<=223:
                C=C+1
            if 224<=int(ip[0])<=239:
                D=D+1
            if 240<=int(ip[0])<=255:
                E= E+1
            #int(ip[0])==10 or (int(ip[0])==172 and 15<int(ip[1])<32) or (int(ip[0])==192 and int(ip[1])==168):
            if int(ip[0])==10 or (int(ip[0])==172 and 16<=int(ip[1])<=31) or (int(ip[0])==192 and int(ip[1])==168):
                pri = pri+1
        else:
            err=err+1

    except:
        break
print"%s %s %s %s %s %s %s"%(A,B,C,D,E,err,pri)
