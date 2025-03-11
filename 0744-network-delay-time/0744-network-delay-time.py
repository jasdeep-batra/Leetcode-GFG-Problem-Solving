class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #we have to check for unconnected node.
        # we can traverse to the longest path and store the max time 
        #for other paths compare it with the max_time
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        s = [(k,0)]
        visit = [0]*(n+1)
        visit[k] = 1
        t = [6001]*(n+1)
        t[k] = 0
        mxt = sys.maxsize
        while s:
            curr,time = heapq.heappop(s)
            if time > t[curr]:
                continue
            for nbr in graph[curr]:
                if (time+nbr[1]) < t[nbr[0]]:                        
                    t[nbr[0]] = time+nbr[1]
                    # visit[nbr[0]] = 0
                    heapq.heappush(s,(nbr[0],t[nbr[0]]))

                        
        print(t)
        # for item in visit:
        #     if not item:
        #         return -1
        return max(t[1:]) if max(t[1:])!=6001 else -1
        






        