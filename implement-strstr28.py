class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        string = 'abc'
        string.find('bc')
        if not haystack.find(needle):
            return -1
        else:
            return haystack.find(needle)

