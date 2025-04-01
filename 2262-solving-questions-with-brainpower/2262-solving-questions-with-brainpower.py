class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # max_point = [0]
        dp = {}
        def helper(i):
            if i>=len(questions):
                return 0
            if i in dp:
                return dp[i]
            jump = questions[i][1]+1
            point = questions[i][0]
            dp[i] = max(point+helper(i+jump),helper(i+1))
            
            return dp[i]
        return helper(0)
        


        