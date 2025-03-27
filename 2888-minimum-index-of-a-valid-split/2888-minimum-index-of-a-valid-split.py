from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the majority element using Moore's Voting Algorithm
        candidate, count = 0, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Step 2: Verify if the candidate is actually the majority element
        freq = nums.count(candidate)
        if freq <= len(nums) // 2:
            return -1  # No valid split possible
        
        # Step 3: Find the minimum index where the left and right parts both contain majority
        left_count = 0
        for i in range(len(nums)):
            if nums[i] == candidate:
                left_count += 1
            
            # Left part should have more than half of its elements as 'candidate'
            if left_count * 2 > (i + 1) and (freq - left_count) * 2 > (len(nums) - i - 1):
                return i
        
        return -1  # No valid split found

# ut: The minimum index where a valid split occurs
