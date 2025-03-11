class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        check = {}
        n = len(s)
        left = 0 
        right = 0
        ans = 0
        for right,right_val in enumerate(s):
            if len(check)!=3:
                if right_val not in check:
                    check[right_val] = 1
                else:
                    check[right_val] +=1
            while(len(check)==3):
                ans+=(n-right)
                print(ans)
                if check[s[left]]==1:
                    del check[s[left]]
                else:
                    check[s[left]]-=1
                left+=1
        return ans


            
            
            


    

        