class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        sm = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            mx = max(nums[i],sm+nums[i])
            sm = max(nums[i],sm+nums[i])
            ans = max(ans,mx)
        return ans

