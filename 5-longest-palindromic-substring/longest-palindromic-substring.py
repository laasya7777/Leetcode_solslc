class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            # expand while inside bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # return the palindrome substring found
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            p1 = expand(i, i)
            p2 = expand(i, i + 1)
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2

        return longest
