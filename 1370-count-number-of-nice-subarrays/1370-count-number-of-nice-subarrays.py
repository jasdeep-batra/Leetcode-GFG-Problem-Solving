class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        mapp = {}
        count = 0
        mapp[0] = 1
        ans  = 0
        for i in range(len(nums)):
            if(nums[i]%2!=0):
                count+=1
            if count in mapp:
                mapp[count]+=1
            else:
                mapp[count] = 1
            if((count-k) in mapp):
                ans+=mapp[count-k]

        return ans

        