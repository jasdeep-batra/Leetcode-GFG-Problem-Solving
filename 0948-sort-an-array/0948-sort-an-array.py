class Solution:
    def counting_sort(self,arr):
        # Find the range of the input numbers
        max_val = max(arr)
        min_val = min(arr)
        range_val = max_val - min_val + 1
        
        # Create count array and output array
        count = [0] * range_val
        output = [0] * len(arr)
        
        # Count the elements
        for num in arr:
            count[num - min_val] += 1
        
        # Cumulative count
        for i in range(1, range_val):
            count[i] += count[i - 1]
        
        # Build the output array
        for num in reversed(arr):
            output[count[num - min_val] - 1] = num
            count[num - min_val] -= 1
        
        return output

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.counting_sort(nums)

        