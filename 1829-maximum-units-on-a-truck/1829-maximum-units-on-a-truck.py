class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        #calculte unit per box then fit it
        unit_arr = [0]*len(boxTypes)
        pq = []
        for i in range(len(boxTypes)):
            bx,ut = boxTypes[i]
            heapq.heappush(pq,(-ut,i))

        
        ans = 0
        while pq and truckSize:
            curr,i = heapq.heappop(pq)
            if boxTypes[i][0]<=truckSize:
                ans+=boxTypes[i][0]*boxTypes[i][1]
                truckSize-=boxTypes[i][0]
            else:
                ans += truckSize*boxTypes[i][1]
                truckSize=0
            
        return ans