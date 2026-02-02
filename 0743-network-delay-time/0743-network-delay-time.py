class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #do we need to create a adj list
        adj_list = defaultdict(list)
        for u,v,w in times:
            adj_list[u].append((v,w))
            
        pq = [(0,k)]
        ans = 0
        weight = [float('inf')]*(n+1)
        weight[k] = 0        
        while pq:
            wei,curr = heapq.heappop(pq)
            if wei > weight[curr]:
                continue
            for v,w in adj_list[curr]:
                if (w+wei) < weight[v]:
                    weight[v] = (w+wei)
                    heapq.heappush(pq,(weight[v],v))

        for i in range(1,n+1):
            if weight[i]==float('inf'):
                return -1
            ans = max(ans,weight[i])

        return ans

        

