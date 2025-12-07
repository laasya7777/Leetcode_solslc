class Solution:
    def countOdds(self, low: int, high: int) -> int:
        mid = (low + high) // 2   
        count = 0

        total = high - low + 1    
        count = total // 2       

        if low % 2 != 0 and high % 2 != 0:
            count += 1

        return count
