class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        original_count = 0
        max_count = 0

        for i in nums:
            if i == 1:
                original_count += 1
                max_count = max(max_count, original_count)
            else:
                original_count = 0
        
        return max_count