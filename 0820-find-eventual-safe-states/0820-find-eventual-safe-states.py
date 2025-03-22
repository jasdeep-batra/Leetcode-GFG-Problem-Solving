class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visit = [0]*len(graph)
        ans = []
        def traverse(node):
            if visit[node]:
                return visit[node]==2

            visit[node] = 1
            for nbr in graph[node]:
                if not traverse(nbr):
                    return False
                
            visit[node] = 2
            return True
        
        for node in range(len(graph)):
            if traverse(node):
                ans.append(node)
        return ans
