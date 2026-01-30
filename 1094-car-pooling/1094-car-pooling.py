class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        print(trips)
        pq = [] #(end point,passenger) (min_heap)
        pas = 0
        for p,s,e in trips:
            while pq and pq[0][0] <= s:
                pas-=heapq.heappop(pq)[1]
            pas+=p
            if pas > capacity:
                return False
            heapq.heappush(pq,(e,p))

        return True
            
            

        return True