class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        ##base condition
        for i in range(n):
            dp[i][i] = 1

        for i in range(0,n-1):
            if(s[i]==s[i+1]):
                
                print("works",i,i+1)
                dp[i][i+1] = 1
                print(dp[i][i+1])

        #window based sliding window
        
        for i in range(2,n):
            for j in range(0,n-i):
                #first element will be j
                #second element will be j + i
                if s[j]==s[j+i] and dp[j+1][j+i-1]==1:
                    dp[j][j+i] = 1

        
        #now backtrack to create a string
        max_len = 0
        m,nn =0,0
        for i in range(0, n):
            for j in range(i, n):
                if dp[i][j] == 1:
                    if (j - i + 1 > max_len):
                        max_len = j - i + 1
                        m = i
                        nn = j


        return s[m:nn+1]

        



            
             
        