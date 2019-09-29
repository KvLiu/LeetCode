import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #s = "abc"
        # s = re.sub('[^0-9a-z]',"",s.lower())
        # print 's=',s
        # return s==s[::-1]

        s = s.lower()
        s = ''.join(re.findall(r'[0-9a-z]', s))
        return s == s[::-1]


a = Solution()
print(a.isPalindrome('A man, a plan, a canal: Panama'))
