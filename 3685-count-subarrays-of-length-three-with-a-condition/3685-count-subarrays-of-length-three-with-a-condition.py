class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        a,b,c =nums[0],nums[1],nums[2]
        cnt = 0
        for i in range(2,len(nums)):
            if (nums[i]+nums[i-2])==(nums[i-1]/2):
                print(nums[i-1]//2)
                cnt+=1
        return cnt
        