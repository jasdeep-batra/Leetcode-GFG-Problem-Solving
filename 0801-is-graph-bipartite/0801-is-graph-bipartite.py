class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0]*n
        def bfs(i):
            if colors[i]:
                return True
            queue = deque([i])
            colors[i] = -1
            while(queue):
                curr = queue.popleft()
                for child in graph[curr]:
                    if colors[curr]==colors[child]:
                        return False
                    elif not colors[child]:
                        colors[child] = -1*colors[curr]
                        queue.append(child)
            return True
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True



                




        