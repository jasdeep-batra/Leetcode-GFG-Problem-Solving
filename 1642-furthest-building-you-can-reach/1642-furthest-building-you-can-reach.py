class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        for i in range(0,len(heights)-1):
            gap = heights[i+1]-heights[i]
            if gap>0:
                heapq.heappush(pq,gap)
                if len(pq) > ladders:
                    brick_need = heapq.heappop(pq)
                    if brick_need > bricks:
                        return i
                    
                    bricks-=brick_need
        
        return len(heights)-1