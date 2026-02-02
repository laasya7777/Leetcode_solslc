from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        if k == 1:
            return nums[0]

        low = SortedList()    # k-1 smallest
        high = SortedList()   # rest
        low_sum = 0

        def rebalance():
            nonlocal low_sum
            while len(low) > k - 1:
                x = low.pop()
                low_sum -= x
                high.add(x)
            while len(low) < k - 1 and high:
                x = high.pop(0)
                low.add(x)
                low_sum += x

        def add(x):
            nonlocal low_sum
            if len(low) < k - 1:
                low.add(x)
                low_sum += x
            elif x < low[-1]:
                y = low.pop()
                low_sum -= y
                high.add(y)
                low.add(x)
                low_sum += x
            else:
                high.add(x)
            rebalance()

        def remove(x):
            nonlocal low_sum
            if x in low:
                low.remove(x)
                low_sum -= x
            else:
                high.remove(x)
            rebalance()

        ans = float('inf')
        left = 1

        for right in range(1, n):
            add(nums[right])

            while right - left > dist:
                remove(nums[left])
                left += 1

            if len(low) == k - 1:
                ans = min(ans, low_sum)

        return nums[0] + ans
