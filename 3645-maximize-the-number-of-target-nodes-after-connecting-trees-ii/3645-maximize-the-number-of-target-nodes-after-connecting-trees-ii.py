class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)
        def make_adj(adj,edges):
            for u,v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj
        adj1 = make_adj(adj1,edges1)
        adj2 = make_adj(adj2,edges2)
        
        def bfs(adj,node):
            queue = deque()
            visited = set()
            even,odd = 0,0
            queue.append((node,0))
            visited.add(node)
            while queue:
                curr,level = queue.popleft()
                if level%2==0:
                    even+=1
                else:
                    odd+=1
                for child in adj[curr]:
                    if child not in visited:
                        queue.append((child,level+1))
                        visited.add(child)

            return (even,odd)
        
        even,odd = 0,0
        for node in range(len(edges1)+1):
            even,odd = bfs(adj1,node)
            break
    
        print(even,odd)
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add(0)
        res = []
        max_odd = 0
        for node in range(len(edges2)+1):
            even1,odd1 = bfs(adj2,node)
            max_odd = max(even1,odd1)
            break
        # print(even,odd,"eyh")
        res = [0]*(len(edges1)+1)
        while queue:
            curr,level = queue.popleft()
            if level%2==0:
                res[curr] = even+max_odd
            else:
                res[curr] = odd+max_odd
            for child in adj1[curr]:
                if child not in visit:
                    queue.append((child,level+1))
                    visit.add(child)
        return res
            
            
        


        # res = []
        res = [max_odd+item[0] for item in first_tree]
        return res



        