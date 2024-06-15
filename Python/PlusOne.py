class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strs = ''.join(str(i) for i in digits)
        output = int(strs) + 1
        return [int(j) for j in str(output)]