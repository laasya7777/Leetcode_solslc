class Solution(object):
    def baseNeg2(self, n):
        if n == 0:
            return "0"

        res = ""
        while n != 0:
            rem = n % -2
            n = n // -2

            if rem < 0:
                rem += 2
                n += 1

            res = str(rem) + res

        return res