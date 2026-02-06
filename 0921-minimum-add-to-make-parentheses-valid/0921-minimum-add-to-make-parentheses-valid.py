class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        #should we determine LVS then substract
        o,c = 0,0
        ans = 0
        for i in s:
            if i=='(':
                o+=1
            if i==')':
                c+=1
            if o==c:
                ans +=2*o
            elif c>o:
                o,c=0,0
        print(ans)
        o,c = 0,0
        for i in reversed(s):
            if i==')':
                c+=1
            if i=='(':
                o+=1
            if o==c:
                ans+= 2*c
            elif o>c:
                o,c=0,0
        print(ans)
        return len(s)-ans