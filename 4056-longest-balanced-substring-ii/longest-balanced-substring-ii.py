class Solution:
    def longestBalanced(self, s: str) -> int:
        pos  = [{(0, 0): -1} for _ in range(4)]
        count = [0, 0, 0]
        res = max(len(list(g)) for k,g in groupby(s))
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            a,b,c = count
            for d, key in zip(pos, [(a-b, b-c), (a-b,c), (b-c, a), (c-a, b)]):
                if key in d:
                    res = max(res, i - d[key])
                else:
                    d[key] = i

        return res  