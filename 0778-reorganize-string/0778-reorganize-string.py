class Solution:
    def reorganizeString(self, s: str) -> str:
        #isn' this ismilar to schedule task\
        frq = Counter(s)
        # print(frq)
        pq = [(-freq,char) for char,freq in frq.items()]
        heapq.heapify(pq)
        index = 0
        ans = ""
        while len(pq)>=2:
            f1,c1 = heapq.heappop(pq)            
            f2,c2 = heapq.heappop(pq)            
            ans+=c1+c2
            if f1+1<0:
                heapq.heappush(pq,(f1+1,c1))
            if f2+1<0:
                heapq.heappush(pq,(f2+1,c2))
        if len(pq):
            f,c = heapq.heappop(pq)
            if f<-1:
                return ""
            ans+=c
        return ans        


