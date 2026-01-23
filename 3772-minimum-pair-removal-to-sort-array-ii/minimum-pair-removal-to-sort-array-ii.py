import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        left = [-1] * n
        right = [-1] * n
        alive = [True] * n

        for i in range(n):
            if i > 0:
                left[i] = i - 1
            if i < n - 1:
                right[i] = i + 1

        # count initial violations
        bad = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                bad += 1

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        ops = 0

        while bad > 0:
            s, i = heapq.heappop(heap)

            if not alive[i] or right[i] == -1:
                continue

            j = right[i]
            if not alive[j]:
                continue

            # stale sum check (CRITICAL)
            if nums[i] + nums[j] != s:
                continue

            pi = left[i]
            nj = right[j]

            # remove old violations
            if pi != -1 and nums[pi] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if nj != -1 and nums[j] > nums[nj]:
                bad -= 1

            # merge
            nums[i] += nums[j]
            alive[j] = False
            right[i] = nj
            if nj != -1:
                left[nj] = i

            # add new violations
            if pi != -1 and nums[pi] > nums[i]:
                bad += 1
            if nj != -1 and nums[i] > nums[nj]:
                bad += 1

            # push new adjacent sums
            if pi != -1:
                heapq.heappush(heap, (nums[pi] + nums[i], pi))
            if nj != -1:
                heapq.heappush(heap, (nums[i] + nums[nj], i))

            ops += 1

        return ops
