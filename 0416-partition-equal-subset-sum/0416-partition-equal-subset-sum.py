class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ%2!=0:
            return False
        memo = [[-1 for i in range(summ//2+1)] for i in range(len(nums))]
        def recursion(i,target):
            if target==0:
                return True
            if i>=len(nums):
                return False
            
            if memo[i][target]!=-1:
                return memo[i][target]
            
            found = recursion(i+1,target-nums[i]) or recursion(i+1,target)
            memo[i][target] = found
            return found
        
        return recursion(0,summ//2)
            
