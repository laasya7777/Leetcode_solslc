from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(row, col, rows, cols, grid, visited):
            return

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        minute = 0
        fresh=0
        visited = []
        for i in range(rows):
            lst = [0] * cols
            visited.append(lst)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh += 1

        while queue:
            row, col, minute = queue.popleft()
            for ur, uc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nr = row + ur
                nc = col + uc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, minute+ 1))

        if fresh > 0:
            return -1
        else:
            return minute
