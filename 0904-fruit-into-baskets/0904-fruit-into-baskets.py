class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #so do we need max window with 2 elements (max freq)
        # we remove the one with less frequency
        mapp = {}
        i = 0
        ans = 0
        for j in range(len(fruits)):
            mapp[fruits[j]] = mapp.get(fruits[j],0)+1
            
            while len(mapp) >2:
                mapp[fruits[i]]-=1
                if mapp[fruits[i]]==0:
                    del mapp[fruits[i]]
                i+=1

            if len(mapp)<=2:
                ans = max(ans,j-i+1)

        return ans