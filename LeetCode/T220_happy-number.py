class Solution:
    def isHappy(self, n):
        num_set = set()
        while n not in num_set:
            num_set.add(n)
            str_num = str(n)
            temp = 0
            for c in str_num:
                temp += int(c)**2
            if temp == 1:
                return True
            else:
                n = temp
        
        return False



s = Solution()
print(s.isHappy(0))