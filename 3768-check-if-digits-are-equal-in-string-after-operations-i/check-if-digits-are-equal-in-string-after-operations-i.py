class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits=[]
        for ch in s:
            digits.append(int(ch))
        while len(digits) > 2:
            new_digits = []
            for i in range(len(digits) - 1):
                new_digits.append((digits[i] + digits[i + 1]) % 10)
            digits = new_digits
        return digits[0] == digits[1]
