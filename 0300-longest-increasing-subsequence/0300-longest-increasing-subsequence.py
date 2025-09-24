class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        inc = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    inc[i] = max(1+inc[j],inc[i])
        # print(i?nc)
        return max(inc)