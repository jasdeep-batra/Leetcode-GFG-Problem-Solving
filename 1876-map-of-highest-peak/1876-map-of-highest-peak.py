from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        queue = deque()
        
        # Initialize the grid and queue
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))  # Start BFS from water cells
                    isWater[i][j] = 0  # Water cells have height 0
                else:
                    isWater[i][j] = -1  # Mark land cells as unvisited
        
        # Directions for adjacent cells
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Perform BFS
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and isWater[ni][nj] == -1:
                    isWater[ni][nj] = isWater[i][j] + 1
                    queue.append((ni, nj))
        
        return isWater
