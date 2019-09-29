# 滑动窗口
# Reference：76. 最小覆盖子串 159. 至多包含两个不同字符的最长子串 340. 至多包含 K 个不同字符的最长子串
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "":
            return 0

        s_len = len(s)
        cur_len = 0
        max_len = 0
        index = 0
        s_set = set()

        for i in range(s_len):
            cur_len += 1
            while s[i] in s_set:
                s_set.remove(s[index])
                cur_len -= 1
                index += 1

            s_set.add(s[i])

            if cur_len > max_len:
                max_len = cur_len

        return max_len


s = Solution()
print(s.lengthOfLongestSubstring(('abbcda')))