class Solution:
    def twoSum(self, nums: list, target: int) -> list:

        d = {}
        for i in range(len(nums)):
            n = nums[i]
            m = target - n
            if m in d.keys():
                return [d[m], i]
            else:
                d[n] = i


s = Solution()
print(s.twoSum([1, 2, 3, 4], 6))