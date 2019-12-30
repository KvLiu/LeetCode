class Solution:
    def isValid(self, s: str) -> bool:

        map = {'}':'{', ']':'[', ')':'('}
        stack = []

        for c in s:
            if c in map.keys():  # 若c是右括号
                if stack: # 若栈中有字符
                    if stack.pop() != map[c]: #取出栈顶并与当前字符是否匹配
                        return False
                else:  # i是右括号，栈中没字符，立马返回false
                    return False
            else: # 若c是左括号
                stack.append(c)

        return not stack


s = Solution()
print(s.isValid("((({}))())()"))


