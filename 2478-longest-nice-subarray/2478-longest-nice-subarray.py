class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        #can we use prefix and ?
        left = 0
        bitor = 0
        ans = 0
        for right in range(len(nums)): 
            while (bitor & nums[right]) !=0:
                bitor ^= nums[left]
                left+=1
            bitor |= nums[right]
            ans = max(ans,(right-left+1))
        return ans
