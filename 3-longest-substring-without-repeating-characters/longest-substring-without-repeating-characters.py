class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = "cadbzabcd"
        n = len(s)
        left, right = 0, 0
        mpp = {}
        maxLen = 0

        while right < n:
            # shrink
            if s[right] in mpp and mpp[s[right]] >= left:
                left = mpp[s[right]] + 1

            maxLen = max(maxLen, right - left + 1)
            mpp[s[right]] = right
            right += 1

        return maxLen
