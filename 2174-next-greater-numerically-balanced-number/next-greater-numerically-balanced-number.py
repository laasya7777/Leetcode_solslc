from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def is_balanced(num):
            count = Counter(str(num))
            for digit, freq in count.items():
                if int(digit) != freq:
                    return False
            return True
        num = n + 1
        while True:
            if is_balanced(num):
                return num
            num += 1
