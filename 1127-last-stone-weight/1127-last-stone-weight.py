class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxstones = [-stone for stone in stones]
        heapq.heapify(maxstones)
        while len(maxstones)>1:
            first = -heapq.heappop(maxstones)
            second = -heapq.heappop(maxstones)
            if first==second:
                continue
            else:
                diff = abs(first-second)
                heapq.heappush(maxstones,-diff)
        return -maxstones[0] if len(maxstones) else 0
