class Solution:
    def longestCommonPrefix(self, strs) :
        prefix = ""
        for a in zip(*strs):
            if len(set(a)) == True: 
                prefix += a[0]
            else: 
                return prefix
        return prefix
