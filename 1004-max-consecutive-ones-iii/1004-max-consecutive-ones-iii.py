class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j = 0,0
        ans = 0
        while j < len(nums):
            if nums[j]==1:
                j+=1
            elif nums[j]==0 and k:
                j+=1
                k-=1
            else:
                ans = max(ans,j-i)
                while k==0:
                    if nums[i]==0:                    
                        k+=1
                    i+=1
        
        ans = max(ans,len(nums)-i)
        return ans

