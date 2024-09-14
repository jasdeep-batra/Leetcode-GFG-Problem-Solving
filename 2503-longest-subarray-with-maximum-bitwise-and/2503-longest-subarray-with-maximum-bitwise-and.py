class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #my idea is that till it is increasing let it be
        #once it start decreasing stop there and start increasing i
        #or we can use prefix and to proceed further
        max_ele = max(nums)
        
        mx_ans = 0
        i=0
        ans  = 0
        while i < len(nums):
            if nums[i]==max_ele:
                ans+=1
            else:
                mx_ans = max(mx_ans,ans)
                # print(mx_ans)
                ans = 0
            i+=1
        mx_ans = max(mx_ans,ans)
        return mx_ans
    #binary search


        

                    




        