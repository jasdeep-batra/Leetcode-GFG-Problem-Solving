class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 1000000007
        nums.sort()
        def count(i,j):
            gap = j-i
            return 2**gap
        n = len(nums)
        i,j = 0,n-1
        ans = 0
        while j>=i:
            if (nums[i]+nums[j])<=target:
                ans+=(count(i,j)%MOD)
                i+=1
            elif (nums[i]+nums[j])>target:
                j-=1
            else:
                i+=1
        return ans%MOD

