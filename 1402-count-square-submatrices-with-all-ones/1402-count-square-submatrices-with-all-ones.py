class Solution:
    def countSquares(self, dp: List[List[int]]) -> int:
        nums = [0]*301
        m,n = len(dp),len(dp[0])
        for i in range(0,m):
            if dp[i][0]==0:
                continue
            nums[1]+=1
        for i in range(1,n):
            if dp[0][i]==0:
                continue
            nums[1]+=1

        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j]==1:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    nums[dp[i][j]]+=1
                    print(dp[i][j])
                
        #suffix sum
        for item in dp:
            print(item)
        nums.sort()
        ans = 0
        summ = 0
        print(nums)
        for item in nums:
            if item==0:
                continue
            summ += item
            ans+=summ
        return ans


        