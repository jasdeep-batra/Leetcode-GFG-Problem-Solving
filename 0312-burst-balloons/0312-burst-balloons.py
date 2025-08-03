class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #backtrack
        n = len(nums)
        nums = [1] + nums + [1]
        @lru_cache(None)
        def recursion(i,j):
            #base condition
            if i>j:
                return 0
            maxi = float('-inf')
            for ind in range(i,j+1):
                cost = nums[ind]*nums[i-1]*nums[j+1] + recursion(i,ind-1) + recursion(ind+1,j)
                maxi = max(maxi,cost)
            return maxi

        return recursion(1,n)
                
                # pop
                #backtrack 
                #get the result
            
                






        