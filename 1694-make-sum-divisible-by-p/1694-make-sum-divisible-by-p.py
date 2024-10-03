class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total_sum = sum(nums)

        if total_sum % p == 0:
            return 0
        if total_sum < p:
            return -1
        target_rem = total_sum % p
        prefix_map = {0: -1}
        current_sum = 0
        min_length = sys.maxsize
        
        for i in range(n):
            current_sum += nums[i]
            need_rem = (current_sum - target_rem) % p
            
            if need_rem in prefix_map:
                j = prefix_map[need_rem]
                min_length = min(min_length, i - j)
            
            prefix_map[current_sum%p] = i
        
        return min_length if min_length<len(nums) else -1