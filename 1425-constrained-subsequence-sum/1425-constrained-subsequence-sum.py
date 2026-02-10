class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        store = [float('-inf')]*len(nums)

        pq = []
        summ = 0
        for j in range(len(nums)):
            #check for the k validity
            while pq and j - pq[0][1]  > k:
                heapq.heappop(pq)
            
            best = -pq[0][0] if pq else 0
            store[j] = nums[j] + max(0,best)
            heapq.heappush(pq,(-store[j],j))
        print(store)
        ans = max(store)
        return ans if ans!=float('-inf') else 0
