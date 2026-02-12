class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # prefix and
        i = 0
        bitor = 0
        ans= 0
        for j in range(len(nums)):
            while (bitor & nums[j]) !=0:
                bitor ^= nums[i]
                i+=1

            bitor|=nums[j]
            ans = max(ans,j-i+1)

        return ans
