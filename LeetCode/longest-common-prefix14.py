class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ""

        min_len = len(strs[0])
        for st in strs:
            if len(st) < min_len:
                min_len = len(st)
        #print "minLen=", min_len
        for i in range(min_len):
            #print "i=", i
            for j in range(1, len(strs)):
                #print "j =", j
                if strs[j][i] != strs[0][i]:
                    return strs[0][0:i]

        return strs[0][0:min_len]

s = Solution()
print (s.longestCommonPrefix(["flower","abc"]))




