class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = map(int, date.split('-'))
    
        monthday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            monthday[1] = 29

        return sum(monthday[:month - 1]) + day