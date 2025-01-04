class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mapp =  {}
        for i in range(len(s)):
            if s[i] not in mapp:
                mapp[s[i]] = [i,i]
            else:
                mapp[s[i]][1] = i
        ans = 0 
        # print(mapp)
        for char,index in mapp.items():
            i,j = index[0],index[1]
            if (i==j) or (j-i+1)<3:
                continue
            container = set()
            for k in range(i+1,j):
                if s[k] not in container:
                    container.add(s[k])
            # print(container)?
            ans+=len(container)

        return ans
            
            
            
