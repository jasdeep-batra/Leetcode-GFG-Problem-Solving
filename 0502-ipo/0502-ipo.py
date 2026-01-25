class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        sort_arr = sorted([(capital[i],profits[i]) for i in range(len(profits))])
        pq = []
        j = 0
        for i in range(k):
            while j<len(sort_arr) and sort_arr[j][0]<=w:
                cap,prof = sort_arr[j]
                heapq.heappush(pq,(-prof))
                j+=1
            
            if not pq:
                break
            w+=-heapq.heappop(pq)

        return w

