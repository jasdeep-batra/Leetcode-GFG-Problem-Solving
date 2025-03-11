class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        check = {}
        a,b,c = 0,0,0
        n = len(s)
        left = 0 
        right = 0
        ans = 0
        for right,right_val in enumerate(s):
            if right_val=='a':
                a+=1
            elif right_val=='b':
                b+=1
            elif right_val=='c':
                c+=1
            while a and b and c:
                ans+=(n-right)
                if s[left]=='a':
                    a-=1
                if s[left]=='b':
                    b-=1
                if s[left]=='c':
                    c-=1
                left+=1
        return ans


            
            
            


    

        