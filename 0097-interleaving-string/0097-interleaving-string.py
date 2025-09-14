class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = dict()
        if len(s1)+len(s2)!=len(s3):
            return False
        def helper(i,j):
            #base condition
            #little bit long
            if i==len(s1) and j==len(s2):
                return True
            ans = False
            if (i,j) in memo:
                return memo[(i,j)]
            if i<len(s1) and s1[i]==s3[i+j]:
            #two option either use char from s1 or s2
                ans = helper(i+1,j) 
            if not ans and j<len(s2) and s2[j]==s3[i+j]:
                ans = helper(i,j+1)
            memo[(i,j)] = ans
            return ans
        
        return helper(0,0)