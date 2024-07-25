class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]*len(nums)
        suff = [1]*len(nums)
        for i in range(1,len(nums)):
            pref[i] = pref[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            suff[i] = suff[i+1]*nums[i+1]

        ans = [0]*len(nums)
        for i in range(0,len(nums)):
            ans[i] = pref[i]*suff[i]
        return ans
        