class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maxSum = nums[0]
        # tmpSum = 0
        # for n in nums:
        #     tmpSum += n
        #     if tmpSum > maxSum:
        #         maxSum = tmpSum
        #     if tmpSum < 0:
        #         tmpSum = 0
        # return maxSum
        l = len(nums)
        if l == 1:
            return nums[0]
        if self.maxSubArray(nums[:-1]) <= 0:
            return nums[l-1]
        if self.maxSubArray(nums[:-1]) >0:
            return self.maxSubArray(nums[:-1]) + nums[l-1]
