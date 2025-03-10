class Solution:

    def dfs(self,graph,hasApple,node,apples,parent):
        time = 0
        for child in graph[node]:         
            if child==parent:
                continue
            child_time=self.dfs(graph,hasApple,child,apples,node)
            if hasApple[child] or child_time>0:
                time+=child_time+2        
        return time
        
        

        
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        return self.dfs(graph,hasApple,0,sum(hasApple),-1)
                





        