class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        from collections import Counter
        MOD = 10**9 + 7
        
        right = Counter(nums)
        left = Counter()
        ans = 0
        
        for val in nums:
            right[val] -= 1
            if right[val] == 0:
                del right[val]
            
            target = val * 2
            ans = (ans + left.get(target, 0) * right.get(target, 0)) % MOD
            
            left[val] += 1
        
        return ans
