class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letters = "abcdefghijklmnopqrstuvwxyz0123456789"
        output = ""
        for char in s:
            if(char.lower() in letters):
                output += char.lower()
        reversedOutput = output[len(output)::-1]
        if output == reversedOutput:
            return True
        else:
            return False