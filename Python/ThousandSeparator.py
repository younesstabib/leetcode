class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        return "{:,.0f}".format(n).replace(',', '.')