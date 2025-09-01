class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def helper(i,j):
            #some base condition
            if j>=len(word2):
                return len(word1)-i
            if i>=len(word1):
                return len(word2)-j
            if (i,j) in memo:
                return memo[(i,j)]
            op = 0
            if word1[i]==word2[j]:
                op = helper(i+1,j+1)
            else:
                op = 1 + min(helper(i+1,j+1),helper(i+1,j),helper(i,j+1))
            memo[(i,j)] = op
            return op
        return helper(0,0)