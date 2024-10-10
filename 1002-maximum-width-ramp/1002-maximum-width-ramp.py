from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # Step 1: Build a decreasing stack
        stack = []
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        # Step 2: Traverse from the end and calculate max width ramp
        ans = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                ans = max(ans, j - stack.pop())
        
        return ans
