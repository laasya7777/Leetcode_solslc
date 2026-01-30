class Trie:
    def __init__(self):
        self.ch = {}
        self.id = -1

class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        n = len(source)

        strings = set(original + changed)
        idx = {s: i for i, s in enumerate(strings)}
        m = len(strings)

        dist = [[INF]*m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            dist[idx[o]][idx[c]] = min(dist[idx[o]][idx[c]], w)

        for k in range(m):
            for i in range(m):
                dik = dist[i][k]
                if dik == INF: continue
                for j in range(m):
                    if dik + dist[k][j] < dist[i][j]:
                        dist[i][j] = dik + dist[k][j]

        rootS = Trie()
        rootT = Trie()

        for s in original:
            node = rootS
            for ch in s:
                node = node.ch.setdefault(ch, Trie())
            node.id = idx[s]

        for s in changed:
            node = rootT
            for ch in s:
                node = node.ch.setdefault(ch, Trie())
            node.id = idx[s]

        dp = [INF]*(n+1)
        dp[n] = 0

        for i in range(n-1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i+1]

            nodeS = rootS
            nodeT = rootT
            j = i

            while j < n:
                cs, ct = source[j], target[j]
                if cs not in nodeS.ch or ct not in nodeT.ch:
                    break
                nodeS = nodeS.ch[cs]
                nodeT = nodeT.ch[ct]

                if nodeS.id != -1 and nodeT.id != -1:
                    c = dist[nodeS.id][nodeT.id]
                    if c < INF:
                        dp[i] = min(dp[i], c + dp[j+1])
                j += 1

        return -1 if dp[0] == INF else dp[0]
