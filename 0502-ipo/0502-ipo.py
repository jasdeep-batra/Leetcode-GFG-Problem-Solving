class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #edge case  
        heap1 = [(capital[i],profits[i]) for i in range(len(profits))]
        heapq.heapify(heap1)#think about storing index
        ans = 0
        heap2 = []
        cc=  w
        while k:
            while heap1 and heap1[0][0] <= cc:
                cap,profit = heapq.heappop(heap1)
                heapq.heappush(heap2,-profit)

            if not heap2:
                break
            k-=1
            maxone = heapq.heappop(heap2)
            cc+=(-maxone)
        return cc





