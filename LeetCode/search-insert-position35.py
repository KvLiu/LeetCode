class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = list()

        if len(nums) == 0:
            return 1
        for i in xrange(nums):
            if nums[i] >= target:
                return i
        nums.pop()
