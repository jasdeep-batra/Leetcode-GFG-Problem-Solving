class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0  # To count how many times the array decreases
        
        # Loop through the array to find how many times nums[i] > nums[i+1]
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                count += 1
                
        # If there's more than one place where nums[i] > nums[i-1], it's not a rotated sorted array
        if count > 1:
            return False
        
        # If count is 0, the array is already sorted
        # If count is 1, check that the last element is less than or equal to the first element
        return count == 0 or nums[-1] <= nums[0]
