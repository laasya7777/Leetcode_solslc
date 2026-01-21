class Solution:
    def minBitwiseArray(self, nums):
        ans = []

        for p in nums:
            if p % 2 == 0:
                ans.append(-1)
                continue

            t = 0
            x = p
            while x & 1:
                t += 1
                x >>= 1

            ans.append(p - (1 << (t - 1)))

        return ans
