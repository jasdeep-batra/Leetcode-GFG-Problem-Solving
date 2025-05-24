class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        score = 0
        ans = 0
        summ = 0
        for j in range(len(nums)):
            summ+=nums[j]
            score = (j+1)*nums[j]
            while summ*(j-left+1)>=k :
                summ-=nums[left]
                left+=1
            ans+=(j-left+1)

        return ans



        