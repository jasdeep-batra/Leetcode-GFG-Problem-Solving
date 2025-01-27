from collections import defaultdict, deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Initialize reachability matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Step 2: Fill in direct prerequisites
        for u, v in prerequisites:
            reachable[u][v] = True
        
        # Step 3: Compute transitive closure (Floyd-Warshall-like algorithm)
        for k in range(numCourses):  # Intermediate node
            for i in range(numCourses):  # Start node
                for j in range(numCourses):  # End node
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True
        
        # Step 4: Answer the queries
        result = []
        for u, v in queries:
            result.append(reachable[u][v])
        
        return result
