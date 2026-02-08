class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #we need prefix here
        if k==0:
            return 0
        prod = 1
        ans = 0

        i,j = 0,0
        while j < len(nums):
            prod *= nums[j]

            while j>i and prod >= k:
                prod = prod//nums[i]
                i+=1
            if prod < k:
                ans+=(j-i+1)

            j+=1

        return ans