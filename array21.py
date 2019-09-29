#https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/21/

class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1):
            for j in nums[i+1: ]:
                if j == nums[i]:
                    nums.remove(j)

        print len(nums)


    removeDuplicates([0,0,1,1,1,2,2,3,3,4])

	
#Solution 2
class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        k=0
        for i in range(1,len(A)):
            if A[i] != A[k]:
                k+=1
                A[k] = A[i]
        
        del A[k+1:len(A)]
        return len(A)
