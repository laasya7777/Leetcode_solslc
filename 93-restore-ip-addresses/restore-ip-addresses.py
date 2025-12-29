class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []

        def backtrack(start, parts, path):
            if parts == 4 and start == len(s):
                res.append(".".join(path))
                return
            if parts == 4 or start == len(s):
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break
                part = s[start:start + length]
                if (part[0] == '0' and length > 1) or int(part) > 255:
                    continue
                backtrack(start + length, parts + 1, path + [part])

        backtrack(0, 0, [])
        return res
