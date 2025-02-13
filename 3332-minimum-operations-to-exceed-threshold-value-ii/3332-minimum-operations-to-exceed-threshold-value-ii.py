import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = []
        for item in nums:
            heapq.heappush(min_heap, item)
        count = 0
        while(min_heap[0] < k):
            first = heapq.heappop(min_heap)
            second = heapq.heappop(min_heap)
            new = min(first, second) * 2 + max(first, second)
            heapq.heappush(min_heap, new)
            count += 1

        return count
