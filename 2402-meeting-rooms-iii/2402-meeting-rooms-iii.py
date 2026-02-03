class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        pq = [(meetings[0][1],0)]
        slot = [i for i in range(1,n)] # also an priority queue
        heapq.heapify(slot)
        freq = [0]*n
        freq[0] = 1
        i = 1
        while i<len(meetings) and pq:
            start,end = meetings[i]
            while pq and pq[0][0] <= start:
                _,room = heapq.heappop(pq)
                heapq.heappush(slot,room)

            if slot:
                room = heapq.heappop(slot)
                heapq.heappush(pq,(end,room))
                freq[room]+=1
            else:
                time,room = heapq.heappop(pq)
                heapq.heappush(pq,(time+end-start,room))
                freq[room]+=1                        
            i+=1
        ind,mx = 0,0
        for j in range(len(freq)):
            if mx < freq[j]:
                mx = freq[j]
                ind = j
        print(freq)
        return ind


            

            
            

