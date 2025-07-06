class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def recursion(i,curr):
            if i>=len(nums):
                if curr==target:
                    return 1
                return 0
            ans = recursion(i+1,curr+nums[i]) + recursion(i+1,curr-nums[i])
            return ans
        return recursion(0,0)

