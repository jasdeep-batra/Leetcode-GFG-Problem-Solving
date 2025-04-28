class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefsum = [0]*len(nums)
        summ = 0
        i= 0
        count = 0
        for j in range(0,len(nums)):
            summ+=nums[j]
            while (summ*(j-i+1)) >= k:
                summ-=nums[i]
                i+=1
            
            count += (j-i+1)
        return count

            




        