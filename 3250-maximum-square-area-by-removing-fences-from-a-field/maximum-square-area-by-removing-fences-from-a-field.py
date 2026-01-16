class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        MOD = 10**9 + 7
    
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]
        hFences.sort()
        vFences.sort()  
        h_dist = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_dist.add(hFences[j] - hFences[i])
       
        v_dist = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_dist.add(vFences[j] - vFences[i])
        
        common = h_dist & v_dist
        if not common:
            return -1
        
        side = max(common)
        return (side * side) % MOD
