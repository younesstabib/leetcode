class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs or any(word == "" for word in strs):
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            for i in range(len(strs[0])):
                for word in strs:
                    if i == len(word) or word[i] != strs[0][i]:
                        return strs[0][:i]
            return strs[0]
        