class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dictt = {}
        summ = sum(nums)
        if summ%2!=0:
            return False
        def recursion(i,target):
            if target==0:
                return True
            if i>=len(nums):
                return False
            
            if (i,target) in dictt:
                return dictt[(i,target)]
            
            found = recursion(i+1,target-nums[i]) or recursion(i+1,target)
            dictt[(i,target)] = found
            return found
        
        return recursion(0,summ//2)
            
