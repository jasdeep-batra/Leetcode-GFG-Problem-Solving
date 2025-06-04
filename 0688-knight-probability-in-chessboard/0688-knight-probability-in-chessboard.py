class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = ((2,1),(1,2),(-2,1),(-1,2),(1,-2),(2,-1),(-1,-2),(-2,-1))
        memo = {}
        if k==0:
            return float(1)
        denom = 8**k
        def helper(i,j,k):
            if k==0:
                return 1
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            count = 0
            for dx,dy in moves:
                x,y = i+dx,j+dy
                if x<0 or x>=n or y<0 or y>=n:
                    continue
                count += helper(x,y,k-1)
            # print(count)
            memo[(i,j,k)] = count
            return count
        # print(denom)

        count = helper(row,column,k)      # stop
        return count/denom
                

        