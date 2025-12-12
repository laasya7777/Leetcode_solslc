from typing import List
import heapq

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        online = [True] * numberOfUsers
        backOnline = []
        nextReturn = [0] * numberOfUsers

        grouped = {}
        for etype, ts, info in events:
            t = int(ts)
            grouped.setdefault(t, []).append((etype, info))

        for t in sorted(grouped.keys()):
            while backOnline and backOnline[0][0] <= t:
                rt, uid = heapq.heappop(backOnline)
                if nextReturn[uid] == rt:
                    online[uid] = True
                    nextReturn[uid] = 0

            for etype, info in grouped[t]:
                if etype == "OFFLINE":
                    uid = int(info)
                    online[uid] = False
                    rt = t + 60
                    nextReturn[uid] = rt
                    heapq.heappush(backOnline, (rt, uid))

            for etype, info in grouped[t]:
                if etype == "MESSAGE":
                    if info == "ALL":
                        for u in range(numberOfUsers):
                            mentions[u] += 1
                    elif info == "HERE":
                        for u in range(numberOfUsers):
                            if online[u]:
                                mentions[u] += 1
                    else:
                        for tk in info.split():
                            uid = int(tk[2:])
                            mentions[uid] += 1

        return mentions
