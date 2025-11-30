class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums)
        rem = total % p

        if rem == 0:
            return 0  

        prefix = 0
        seen = {0: -1}  
        ans = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            need = (prefix - rem) % p

            if need in seen:
                ans = min(ans, i - seen[need])

            seen[prefix] = i

        return ans if ans < len(nums) else -1
