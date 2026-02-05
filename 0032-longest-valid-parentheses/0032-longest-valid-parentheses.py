class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s=="":
            return 0

        o,c = 0,0
        ans = 0
        for i in range(len(s)):
            if s[i]=='(':
                o+=1
            elif s[i]==')':
                c+=1
            if o==c:
                ans = max(ans,2*c)
            elif c>o:
                o=c=0
            
        orr,cr = 0,0
        for i in range(len(s)-1,-1,-1):
            if s[i]==')':
                cr+=1
            elif s[i]=='(':
                orr+=1

            if cr==orr:
                ans = max(ans,2*orr)
            elif orr>cr:
                orr=cr=0

        
        return ans



        return ans

            




