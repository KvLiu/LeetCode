class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif str(x) == str(x)[::-1]:
            return True
        else:
            return False

a = Solution()
print (a.isPalindrome(1221))
