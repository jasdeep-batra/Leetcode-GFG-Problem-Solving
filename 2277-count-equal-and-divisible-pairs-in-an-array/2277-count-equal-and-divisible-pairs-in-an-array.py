class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i]==nums[j]) and ((i*j)%k==0):
                    ans+=1
        return ans
        