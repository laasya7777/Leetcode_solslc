class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []

        val1 = val2 = None
        count1 = count2 = 0

        for num in nums:
            if num == val1:
                count1 += 1
            elif num == val2:
                count2 += 1
            elif count1 == 0:
                val1 = num
                count1 = 1
            elif count2 == 0:
                val2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        for val in [val1, val2]:
            if val is not None and nums.count(val) > len(nums) // 3:
                result.append(val)

        return result
