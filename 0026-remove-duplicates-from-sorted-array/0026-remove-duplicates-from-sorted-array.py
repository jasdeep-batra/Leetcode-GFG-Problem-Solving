class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 1
        while i<len(nums) and nums[i]!=101:
            if nums[i]==nums[i-1]:
                k+=1
                val = nums.pop(i)
                nums.append(101)
                continue
            i+=1
        # print(nums)
        return len(nums)-k
        
        