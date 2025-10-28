class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for curr in range(n):
            if nums[curr] != 0:
                continue

            left = curr
            right = n - 1
            temp = nums[:]          
            direction = 1

            while 0 <= left <= right:
                if temp[left] == 0:
                    left += direction
                else:
                    temp[left] -= 1
                    direction = -direction
                    left += direction

            if all(x == 0 for x in temp):
                ans += 1

        
            left = curr
            right = n - 1
            temp = nums[:]
            direction = -1

            while 0 <= left <= right:
                if temp[left] == 0:
                    left += direction
                else:
                    temp[left] -= 1
                    direction = -direction
                    left += direction

            if all(x == 0 for x in temp):
                ans += 1

        return ans
