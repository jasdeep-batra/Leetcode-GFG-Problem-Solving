class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapp = {}
        for item in t:
            if item not in mapp:
                mapp[item] = 1
            else:
                mapp[item]+=1
        
        i,j = 0,0
        count = len(t)
        min_length = float('inf')
        ans = ""
        start = 0
        while(j<len(s)):
            if s[j] in mapp:
                mapp[s[j]] -= 1
                if mapp[s[j]]>=0:
                    count-=1
                
            while count==0:
                if j-i+1 < min_length:
                    min_length = j-i+1
                    start = i
                if s[i] in mapp:
                    mapp[s[i]]+=1   
                    if mapp[s[i]]>0:                        
                        count+=1
                i+=1
            j+=1 
        return s[start:start + min_length] if min_length != float('inf') else ""


            



        