class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        dist1 = [-1]*len(edges)
        dist2 = [-1]*len(edges)
        def BFS(node,dist):
            dist[node] = 0
            queue = deque()
            visit = set()
            queue.append((node,0))
            visit.add(node)
            while queue:
                curr,d = queue.popleft()
                child = edges[curr]
                if child!=-1 and child not in visit:
                    dist[child] = d+1
                    queue.append((child,d+1))
                    visit.add(child)
        BFS(node1,dist1)
        BFS(node2,dist2)
        ans = sys.maxsize
        ansi = -1
        for i in range(len(dist1)):
            index = 0
            if dist1[i]!=-1 and dist2[i]!=-1:
                maxe = max(dist1[i],dist2[i])
                index = i

                if maxe < ans:
                    ans = maxe
                    ansi = i

            
        print(dist1)
        print(dist2)
        
        return ansi


