class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        project = sorted([(capital[i],profits[i]) for i in range(len(profits))])
        # project = sorted(zip(capitals,profits))

        pq = []
        i = 0
        while k>0:
            while i < len(project) and project[i][0] <= w:
                heapq.heappush(pq,-project[i][1])
                i+=1
            
            if not pq:
                break
            w+=-heapq.heappop(pq)
            k-=1
        
        return w
