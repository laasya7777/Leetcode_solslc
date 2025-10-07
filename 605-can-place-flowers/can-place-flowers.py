class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                left_is_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_is_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
    
                if left_is_empty and right_is_empty:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0
