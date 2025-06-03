class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        ans = [0]
        memo = {}
        def recursion(i,step):
            if i==len(nums)-1:
                return 0
            if i in memo:
                return memo[i]
            ans = -1
            for ind in range(i+1,len(nums)):
                diff = (nums[ind] - nums[i])
                if (-1*target)<=diff<=target:
                    steps = recursion(ind,step+1)
                    if steps!=-1:
                        ans = max(ans,steps+1)

                    
            memo[i] = ans
            return memo[i]

        recursion(0,0)
        return memo[0] if memo[0]!=-1 else -1
