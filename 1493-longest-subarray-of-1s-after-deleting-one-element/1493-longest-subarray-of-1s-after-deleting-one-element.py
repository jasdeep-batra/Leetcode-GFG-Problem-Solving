class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        delete = 1
        ans = 0
        for j in range(len(nums)):
            if nums[j]==0:
                delete-=1
            
            while delete<0:
                if nums[i]==0:
                    delete+=1
                i+=1

            ans = max(ans,j-i)
        return ans