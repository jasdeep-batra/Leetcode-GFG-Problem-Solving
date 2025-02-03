class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        stack = []
        max_len = 0
        inc_len = 1
        dec_len = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                inc_len+=1
                dec_len = 1
                max_len = max(max_len,inc_len)
            elif nums[i] < nums[i-1]:
                inc_len = 1
                dec_len+=1
                max_len = max(max_len,dec_len)
            else:
                inc_len = 1
                dec_len = 1
        max_len = max(max_len,inc_len,dec_len)
        return max_len

                





        