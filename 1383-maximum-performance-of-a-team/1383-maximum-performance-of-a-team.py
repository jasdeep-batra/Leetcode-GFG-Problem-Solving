class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD=10**9+7
        arr = sorted([(efficiency[i],speed[i]) for i in range(len(speed))],reverse=True)        
        pq = []
        curr_speed = 0
        j = 0
        ans = 0
        while j < len(arr):
            e,s = arr[j]
            curr_speed+=s
            heapq.heappush(pq,s)
            if len(pq) > k:
                curr_speed-=heapq.heappop(pq)
            ans = max(e*(curr_speed),ans)
            j+=1
        return ans%MOD
        

            
