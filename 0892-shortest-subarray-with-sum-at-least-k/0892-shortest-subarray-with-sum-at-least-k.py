from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        # Compute prefix sums
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Deque to store indices of prefix sums
        dq = deque()
        ans = float('inf')  # Initialize to a large value
        
        for j in range(n + 1):
            # Check if there's a valid subarray
            while dq and prefix_sum[j] - prefix_sum[dq[0]] >= k:
                ans = min(ans, j - dq.popleft())
            
            # Maintain deque in increasing order of prefix sums
            while dq and prefix_sum[j] <= prefix_sum[dq[-1]]:
                dq.pop()
            
            dq.append(j)
        
        return ans if ans != float('inf') else -1
