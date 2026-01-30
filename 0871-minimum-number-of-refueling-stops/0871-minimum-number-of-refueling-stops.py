class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.sort()
        stations.append([target,0])
        if target==startFuel:
            return 0
        if not stations:
            return -1
        pq = []
        ans = 0
        i = 0        
        d = startFuel
        while i<len(stations):
            if stations[i][0] <= d:
                heapq.heappush(pq,(-stations[i][1],stations[i][0]))
                i+=1
            else:
                if not pq:
                    return -1
                station = heapq.heappop(pq)
                d+=-station[0]
                ans+=1
        # if target > d:
        #     return -1
        return ans
