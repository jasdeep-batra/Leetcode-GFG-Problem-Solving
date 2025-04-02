class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        #are we going to use kadane algorithm
        max_ans = [-1000]
        for i in range(0,len(nums)-2):
            first = nums[i]
            for j in range(i+1,len(nums)-1):
                second = nums[j]
                if first > second:
                    for k in range(j+1,len(nums)):
                        max_ans[0] = max(max_ans[0],nums[k]*(first-second))
        return max_ans[0] if max_ans[0]>0 else 0


        