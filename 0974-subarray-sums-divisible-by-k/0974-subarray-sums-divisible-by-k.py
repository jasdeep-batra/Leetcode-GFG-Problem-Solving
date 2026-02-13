class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #do we need to use prefix sum?
        mapp = {0:1}
        i = 0
        ans = 0
        summ = 0
        for j in range(len(nums)):
            summ+=nums[j]
            
            rem = summ%k
            if summ%k < 0:
                rem+=k
            ans += mapp.get(rem,0)
            mapp[rem] = mapp.get(rem,0)+1

        return ans


