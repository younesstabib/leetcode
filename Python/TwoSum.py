class Solution(object):
    def twoSum(self, nums, target):
        for index, a in enumerate(nums):
            for idx, b in enumerate(nums):
                if(index != idx):
                    if(a + b) == target:
                        return [index, idx]