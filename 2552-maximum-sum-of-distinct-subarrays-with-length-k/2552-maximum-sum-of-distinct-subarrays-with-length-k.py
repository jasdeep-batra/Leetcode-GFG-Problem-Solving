from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sliding_window = {}
        ans = 0
        current_sum = 0
        n = len(nums)
        
        for i in range(n):
            # Add the current element to the sliding window and update the sum
            if nums[i] in sliding_window:
                sliding_window[nums[i]] += 1
            else:
                sliding_window[nums[i]] = 1
            current_sum += nums[i]
            
            # Remove the element that goes out of the window
            if i >= k:
                outgoing = nums[i - k]
                if sliding_window[outgoing] == 1:
                    del sliding_window[outgoing]
                else:
                    sliding_window[outgoing] -= 1
                current_sum -= outgoing
            
            # Check if the window is valid and update the answer
            if len(sliding_window) == k:
                ans = max(ans, current_sum)
        
        return ans
