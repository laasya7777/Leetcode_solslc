from collections import deque

class Solution:
    def minMutation(self, startGene, endGene, bank):
        bank = set(bank)
        if endGene not in bank:
            return -1

        q = deque([(startGene, 0)])
        visited = {startGene}
        genes = ['A', 'C', 'G', 'T']

        while q:
            curr, steps = q.popleft()
            if curr == endGene:
                return steps

            for i in range(8):
                for g in genes:
                    if g == curr[i]:
                        continue
                    nxt = curr[:i] + g + curr[i+1:]
                    if nxt in bank and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))

        return -1
