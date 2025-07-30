class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod = 1
        start = 0
        ans = 0
        for i in range(len(nums)):
            prod*=nums[i]
            while prod>=k and start<=i:
                prod//=nums[start]
                start+=1
            
            ans+=(i-start+1)
        return ans


