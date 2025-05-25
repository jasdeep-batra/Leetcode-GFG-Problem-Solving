class Solution:
    def minimumOperations(self, numss: List[int]) -> int:
        
        nums = sorted(list(set(numss)))

        max_num = max(nums)
        diff = 0
        ops = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            diff=(nums[i]-nums[i-1])
            ops+=1
            if diff >= max_num:
                return ops
        return ops
            
            
