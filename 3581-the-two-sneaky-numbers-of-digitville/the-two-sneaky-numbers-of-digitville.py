from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()   
        stack = []     

        for num in nums:           
            if num in seen:
                stack.append(num)  
                if len(stack) == 2:  
                    break
            else:
                seen.add(num)

        return stack
