class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(kk):
            if kk<=0:
                return 0
            mapp = {}

            i = 0
            ans = 0
            for j in range(len(nums)):
                mapp[nums[j]] = mapp.get(nums[j],0)+1

                while len(mapp) > kk:
                    mapp[nums[i]]-=1
                    if mapp[nums[i]]==0:
                        del mapp[nums[i]]
                    i+=1

                ans+= (j-i+1)
            return ans

        
        return helper(k)-helper(k-1)
                

