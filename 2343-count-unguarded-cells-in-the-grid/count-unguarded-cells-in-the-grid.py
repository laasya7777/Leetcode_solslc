from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
       
        grid = [[0] * n for _ in range(m)]

        for r, c in guards:
            grid[r][c] = 2
  
        for r, c in walls:
            grid[r][c] = 3
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)] 
        
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 2 or grid[nr][nc] == 3: 
                        break
                    if grid[nr][nc] == 0: 
                        grid[nr][nc] = 1
                    nr += dr
                    nc += dc
        
        
        return sum(grid[i][j] == 0 for i in range(m) for j in range(n))
