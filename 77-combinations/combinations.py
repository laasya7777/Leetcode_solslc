class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = list(range(1, k + 1))
        res = []

        while True:
            res.append(comb[:])

            i = k - 1
            while i >= 0 and comb[i] == n - k + i + 1:
                i -= 1

            if i < 0:
                break

            comb[i] += 1
            for j in range(i + 1, k):
                comb[j] = comb[j - 1] + 1

        return res
