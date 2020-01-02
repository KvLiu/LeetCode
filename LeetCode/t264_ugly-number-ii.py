# 【笔记】三指针法。一部分是丑数数组，另一部分是权重2，3，5。下一个丑数，定义为丑数数组中的数乘以权重，所得的最小值。
# 那么，2该乘以谁？3该乘以谁？5该乘以谁？
# 定义三个变量 idx2 idx3 idx5, 2,3和5要分别乘以list中的第idx2 idx3和idx5个数
# 其二，当命中下一个丑数时，说明该指针指向的丑数 乘以对应权重所得积最小。此时，指针应该指向下一个丑数。
# 其三，要使用三个并列的`if`让指针指向一个更大的数，不能用`if-else`。因为有这种情况：
# - 丑数6，可能由于丑数2乘以权重3产生；也可能由于丑数3乘以权重2产生。
# - 丑数10，... 等等。

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglyNumList = [1]
        idx2 = idx3 = idx5 = 0
        for i in range(n - 1):
            uglyNumList.append(min(uglyNumList[idx2]*2, uglyNumList[idx3]*3, uglyNumList[idx5]*5))
            print(uglyNumList)
            if uglyNumList[idx2]*2  == uglyNumList[-1]:
                idx2 += 1
            if uglyNumList[idx3]*3 == uglyNumList[-1]:
                idx3 += 1
            if uglyNumList[idx5]*5 == uglyNumList[-1]:
                idx5 += 1
        return uglyNumList[-1]
 
if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(10))

