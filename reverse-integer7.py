class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        while x%10 == 0:
            x/=10

        if str(x).startswith('-'):
            x = int('-' + str(x)[1:][::-1])
            if x < 2**31:
                return 0
            else:
                return x
        else:
            x = int(str(x)[::-1])
            if x > 2**31-1:
                return 0
            else:
                return x

a = Solution()
print (a.reverse(-1230))
