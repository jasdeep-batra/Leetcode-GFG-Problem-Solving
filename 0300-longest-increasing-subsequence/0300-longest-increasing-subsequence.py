class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums)+1)
        for i in range(len(dp)-1,0,-1):
            for j in range(i+1,len(dp)):
                if nums[i-1] < nums[j-1]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(max(dp),1)




