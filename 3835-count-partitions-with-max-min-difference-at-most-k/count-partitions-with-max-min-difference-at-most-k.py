from collections import deque

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        dp[0] = 1
        prefix = [0] * (n + 1)
        prefix[0] = 1

        min_q = deque()
        max_q = deque()
        left = 0

        for right in range(n):
            while min_q and nums[min_q[-1]] > nums[right]:
                min_q.pop()
            min_q.append(right)

            while max_q and nums[max_q[-1]] < nums[right]:
                max_q.pop()
            max_q.append(right)

            while nums[max_q[0]] - nums[min_q[0]] > k:
                if min_q[0] == left:
                    min_q.popleft()
                if max_q[0] == left:
                    max_q.popleft()
                left += 1

            dp[right + 1] = prefix[right]
            if left > 0:
                dp[right + 1] = (dp[right + 1] - prefix[left - 1]) % MOD

            prefix[right + 1] = (prefix[right] + dp[right + 1]) % MOD

        return dp[n]
