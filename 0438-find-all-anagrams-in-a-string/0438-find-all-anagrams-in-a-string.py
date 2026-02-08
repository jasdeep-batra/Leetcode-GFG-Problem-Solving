class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # we know the lenght of sliding window 
        #count = 0
        mapp = {}
        for i,c in enumerate(p):
            mapp[c]=mapp.get(c,0)+1

        count = 0

        i,j = 0,0
        res = []
        k = len(p)
        while j<len(s):
            if (j-i+1)<=k:
                if s[j] in mapp:
                    mapp[s[j]]-=1
                
                    if mapp[s[j]]>=0:
                        count+=1
                j+=1
                print(mapp)
                print(count)
                if count==len(p):
                    res.append(i)
            else:
                print(i)
                if s[i] in mapp:
                    mapp[s[i]]+=1
                    if mapp[s[i]]>0:
                        count-=1
                i+=1

        return res
        