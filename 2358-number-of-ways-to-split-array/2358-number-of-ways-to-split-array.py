class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        #could problem of prefix and suffix sum 
        ans = 0
        prefix_sum = [0]*(len(nums)+1)
        for index,item in enumerate(nums):
            prefix_sum[index+1] = item + prefix_sum[index]

        for i in range(1,len(nums)):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[-1] - prefix_sum[i]
            if left_sum >= right_sum:
                ans += 1 
        # print(prefix_sum)
        return ans

        
        