class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        summ = 0
        pq = [(0,-1)]
        for j in range(len(nums)):
            summ+=nums[j]
            while pq and (summ - pq[0][0]) >=k:
                ans = min(ans,j-pq[0][1])
                heapq.heappop(pq)

            heapq.heappush(pq,((summ,j)))
        return ans if ans!=float('inf') else -1



