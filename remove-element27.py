class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        while nums.count(val) != 0:
            nums.remove(val)
        return nums

s = Solution()
print(s.removeElement([0,1,2,2,3,0,4,2],2))
