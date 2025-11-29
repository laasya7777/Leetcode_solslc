class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
      
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        a = abs(dividend)
        b = abs(divisor)
        
        result = 0
        
        
        while a >= b:
            temp = b
            count = 1
            while a >= (temp << 1):
                temp <<= 1
                count <<= 1
            a -= temp
            result += count
        
        return sign * result
