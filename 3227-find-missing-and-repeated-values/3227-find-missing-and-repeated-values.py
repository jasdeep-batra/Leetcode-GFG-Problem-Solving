class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cache = [0]*(n*n+1)
        for i in range(n):
            for j in range(n):
                cache[grid[i][j]] +=1

        return [i for i in range(1,n*n+1) if cache[i]==2] + [i for i in range(1,n*n+1) if cache[i]==0]
        