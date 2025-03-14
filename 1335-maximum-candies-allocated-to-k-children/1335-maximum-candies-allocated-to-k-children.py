from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        
        def canDist(mid):
            count = sum(item // mid for item in candies)
            return count >= k

        if total < k:  # If there aren't enough candies to give at least one to each child
            return 0

        i, j = 1, max(candies)  # Use max(candies) instead of sum(candies)
        ans = 0

        while i <= j:  # Fix condition
            mid = (i + j) // 2
            if canDist(mid):
                ans = mid  # Store the valid value
                i = mid + 1  # Move right to maximize the number of candies per child
            else:
                j = mid - 1  # Move left if we can't distribute at this size

        return ans
