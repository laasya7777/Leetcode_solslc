from math import gcd
from functools import reduce

class Solution:
    def minOperations(self, nums):
        n = len(nums)
      
        total_gcd = reduce(gcd, nums)
        if total_gcd != 1:
            return -1
        

        count_ones = nums.count(1)
        if count_ones > 0:
            return n - count_ones
    
        min_len = float('inf')
        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break  
        
        return (min_len - 1) + (n - 1)
