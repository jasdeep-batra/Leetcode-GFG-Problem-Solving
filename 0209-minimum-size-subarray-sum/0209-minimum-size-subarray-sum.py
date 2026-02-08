class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #minimal length to be determined.
        #are all elements positive #how to handle negetive values.
        summ=0
        i,j=0,0
        ans = float('inf')
        while j<len(nums):
            summ+=nums[j]

            while i<=j and summ >=target:
                ans = min(ans,j-i+1)
                summ-=nums[i]
                i+=1                
            j+=1
        
        return ans if ans!=float('inf') else 0