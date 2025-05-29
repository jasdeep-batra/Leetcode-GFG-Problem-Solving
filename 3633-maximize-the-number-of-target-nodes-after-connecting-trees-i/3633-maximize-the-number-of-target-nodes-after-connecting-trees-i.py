class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], K: int) -> List[int]:
        adj = defaultdict(list)
        adj2 = defaultdict(list)
        for u,v in edges1:
            adj[u].append(v)
            adj[v].append(u)
        for u,v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        
        def bfs(root,k,adjList):
            queue =  deque()
            ans = 0
            visited = set()
            visited.add(root)
            queue.append((root,-1))
            while queue and k>=0:
                size = len(queue)
                ans+=size
                while size:
                    curr,level = queue.popleft()
                    visited.add(curr)
                    for child in adjList[curr]:  
                        if child not in visited:
                            visited.add(child)
                            queue.append((child,level+1)) 
                    size-=1
                k-=1
            return ans
        
        res = []
        for i in range(0,(len(edges1)+1)):
            res.append(bfs(i,K,adj))
        ans = 0
        print(res)
        for i in range(0,len(edges2)+1):
            ans = max(ans,bfs(i,K-1,adj2))
        for i in range(len(res)):
            res[i]+=ans
        return res
        

        

        
        