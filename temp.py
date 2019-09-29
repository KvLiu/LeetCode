# -*- coding: utf-8 -*-
class Solution:
    def isHappy(self, n):
        num_set = set()
        while n not in num_set:
            num_set.add(n)
            print(num_set)
            tmp_sum = 0
            # 该数不为0，前者为个位数不为0情况，后面为个位数为0情况
            while n%10 != 0 or n//10 != 0: 
                tmp_sum += (n%10)**2
                n = n//10
            print(tmp_sum)
            if tmp_sum == 1:
                return True
            else:
                n = tmp_sum
        
        return False



s = Solution()
print(s.isHappy(16))