class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        splitted_str = s.split()
        splitted_str = [tab[::-1] for tab in splitted_str]
        splitted_str.sort()
        splitted_str = [tab[::-1] for tab in splitted_str]
        splitted_str = [s[:-1] for s in splitted_str]
        print(splitted_str)
        return ' '.join(splitted_str)