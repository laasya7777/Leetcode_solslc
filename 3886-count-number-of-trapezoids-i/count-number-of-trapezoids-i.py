class Solution:
    def countTrapezoids(self, points):
        from collections import defaultdict
        
        MOD = 10**9 + 7
        y_count = defaultdict(int)
        for x, y in points:
            y_count[y] += 1
        
        ans = 0
        prefix_sum = 0
        for cnt in y_count.values():
            if cnt >= 2:
                val = cnt * (cnt - 1) // 2  # C(cnt, 2)
                ans = (ans + val * prefix_sum) % MOD
                prefix_sum = (prefix_sum + val) % MOD
        
        return ans
