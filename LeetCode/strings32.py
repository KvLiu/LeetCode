class Solution(object):
    def reverseString(s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        # for i in range(len(s)/2):
        #     s[i],s[len(s)-i-1] = s[len(s)-i-1],s[i]
        #
        # print s
        #ret = s[::-1]
        #return ret
        s = s[::-1]
        return s
        #return res
        #print res
        #print s

    print (reverseString(['a','b','c','d','e']))
    reverseString(['h','e','l','l','o'])
