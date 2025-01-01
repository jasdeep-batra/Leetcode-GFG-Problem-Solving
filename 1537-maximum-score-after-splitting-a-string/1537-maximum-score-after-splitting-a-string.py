class Solution:
    def maxScore(self, s: str) -> int:
        # zero on left and one on right
        #formula since it is binary
        zero = 0
        ans = 0
        one = s.count('1')
        for i in range(len(s)-1):
            if s[i]=='0':
                zero+=1
            else:
                one-=1
            ans = max(ans,zero+one)
        return ans

        

        