class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #edge conditions

        def atmost(goall):
            if( goall < 0):
                return 0
            summ = 0
            ans = 0
            i = 0
            for j in range(len(nums)):
                summ+=nums[j]
                while summ > goall:
                    summ-=nums[i]        
                    i+=1    


                ans += (j-i+1)

            return ans  




        return atmost(goal) - atmost(goal-1)
