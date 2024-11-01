class Solution:
    def makeFancyString(self, ss: str) -> str:
        #can we use window of size 3
        count = 0
        count = 1
        last = 0
        s = list(ss)
        for i in range(1,len(s)):
            if s[last]==s[i]:
                count+=1
                if count==3:
                    s[i] = '-1'
                    count -= 1
                    continue
            elif s[i]!=s[i-1]:
                last = i
                count = 1
        
        ans = "".join(x for x in s if x != "-1")
        return ans

            
            

            




        