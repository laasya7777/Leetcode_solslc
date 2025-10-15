class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        j = 0     
        for i in word1:
            res += i  
            if j < len(word2):
                res += word2[j]   
                j += 1   
        res += word2[j:]
        return res
