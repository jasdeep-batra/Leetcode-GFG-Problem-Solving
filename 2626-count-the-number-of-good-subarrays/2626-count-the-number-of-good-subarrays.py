class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        dictt = {}
        ans,i = 0,0

        for item in nums:
            if item not in dictt:
                dictt[item] = 0
            dictt[item]+=1
            if dictt[item]>1:
                k-=dictt[item]-1
            
            while k<=0:
                dictt[nums[i]]-=1
                k+=dictt[nums[i]]
                i+=1
            ans+=i
        return ans
            
            

        
        