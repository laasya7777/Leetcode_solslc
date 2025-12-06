class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        
        for i, val in enumerate(nums):
            if left_sum == total - left_sum - val:
                return i
            left_sum += val
        
        return -1
