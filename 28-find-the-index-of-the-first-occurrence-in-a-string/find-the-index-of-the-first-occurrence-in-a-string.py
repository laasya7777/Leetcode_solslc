class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0  

        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1
