from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])  # Number of columns
        dp = [[0] * n for _ in range(2)]  # DP matrix to track max scores
        
        # Calculate the cumulative sum for both rows
        for j in range(2):  # For both rows
            for i in range(n):  # For all columns
                if i == 0:  # First column initialization
                    dp[j][i] = grid[j][i]
                else:
                    dp[j][i] = dp[j][i - 1] + grid[j][i]

        # Initialize the result with a very large value
        result = float('inf')
        
        # Try each column as the crossing point
        for i in range(n):
            # Calculate the points for the other robot
            top_remaining = dp[0][n - 1] - dp[0][i]  # Remaining on the top row
            bottom_visited = dp[1][i - 1] if i > 0 else 0  # Already visited on the bottom row

            # Maximum points the second robot can collect
            max_score = max(top_remaining, bottom_visited)
            result = min(result, max_score)  # Minimize the maximum score
            
        return result
