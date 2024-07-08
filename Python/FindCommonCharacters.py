class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output = []
        
        for char in set(words[0]):
            min_count = words[0].count(char)
            for word in words[1:]:
                min_count = min(min_count, word.count(char))
            
            output.extend([char] * min_count)
        
        return output