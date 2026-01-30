class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        freq = Counter(s)
        pq = []
        i = 0
        for key,val in freq.items():
            heapq.heappush(pq,(-val,key))

        while len(pq)>=2:
            f1,c1 = heapq.heappop(pq)
            f2,c2 = heapq.heappop(pq)
            ans+=c1+c2

            if f1+1 < 0:
                heapq.heappush(pq,(f1+1,c1))

            if f2+1 < 0:
                heapq.heappush(pq,(f2+1,c2))

        while pq and pq[0][0]>=-1:
            ans+=heapq.heappop(pq)[1]
        
        if pq:
            return ""
        return ans        
        
        