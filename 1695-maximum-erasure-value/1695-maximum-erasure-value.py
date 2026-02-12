class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mapp = {}
        ans = 0
        summ = 0
        i = 0
        for j in range(len(nums)):    
            if nums[j] in mapp and mapp[nums[j]] >= 0:
                ans = max(ans,summ)
                while i <= mapp[nums[j]]:
                    summ-=nums[i]
                    mapp[nums[i]] = -1

                    i+=1
            mapp[nums[j]] = j    
            summ+=nums[j]
        return max(ans,summ)