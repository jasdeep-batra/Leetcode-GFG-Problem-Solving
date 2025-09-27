class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #store the frequency in the maxheap
        mapp = defaultdict(int)
        for item in nums:
            mapp[item]+=1
        
        max_heap = [] #maxheap
        for num,freq in mapp.items():
            heapq.heappush(max_heap,(-freq,num))
        # print(max_heap)
        ans = []
        while k:
            freq,num = heapq.heappop(max_heap)
            ans.append(num)
            k-=1
        return ans
