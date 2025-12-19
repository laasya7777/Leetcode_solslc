from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        
        secret = set([0, firstPerson])
        i = 0
        
        while i < len(meetings):
            time = meetings[i][2]
            graph = defaultdict(list)
            people = set()
            
            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                people.add(x)
                people.add(y)
                i += 1
            
            visited = set()
            
            for p in people:
                if p in visited:
                    continue
                
                queue = deque([p])
                component = set([p])
                visited.add(p)
                has_secret = p in secret
                
                while queue:
                    cur = queue.popleft()
                    for nei in graph[cur]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
                            component.add(nei)
                            if nei in secret:
                                has_secret = True
                
                if has_secret:
                    secret.update(component)
        
        return list(secret)
