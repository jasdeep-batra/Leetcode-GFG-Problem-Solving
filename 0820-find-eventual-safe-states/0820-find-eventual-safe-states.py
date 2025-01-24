class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0] * n  # 0 = unvisited, 1 = visiting, 2 = safe
        result = []

        def dfs(node):
            if visited[node] != 0:  # Already processed
                return visited[node] == 2  # Return True if it's safe
            visited[node] = 1  # Mark as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):  # If any neighbor is not safe
                    return False
            visited[node] = 2  # Mark as safe
            return True

        for i in range(n):
            if dfs(i):  # If the node is safe, add it to the result
                result.append(i)
        
        return result
