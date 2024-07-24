class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1,len(nums)):
            nums[i] = max(i+nums[i], nums[i-1])

        i = 0
        ans = 0
        while i< n-1:
            ans+=1
            i = nums[i]

        return ans



        