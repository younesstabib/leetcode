class Solution(object):
    def romanToInt(self, s):
        romNum = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        previousVal = 0

        for c in reversed(s):
            val = romNum[c]
            if val < previousVal:
                total -= val
            else:
                total += val
            previousVal = val
        
        return total