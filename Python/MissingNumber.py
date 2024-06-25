class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        sum_nums = len_nums * (len_nums + 1) // 2
        actual_sum = sum(nums)
        return sum_nums - actual_sum