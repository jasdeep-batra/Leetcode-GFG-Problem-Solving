class Solution:
    def maximumJumps(self,nums, target):
        n = len(nums)
        dp = [-1] * n  # dp[i] = max jumps from i to end
        dp[-1] = 0  # Base case: already at the end (0 jumps needed)

        for i in range(n - 2, -1, -1):  # Iterate from second-last to first
            max_jumps = -1
            for j in range(i + 1, n):
                if -target <= nums[j] - nums[i] <= target:
                    if dp[j] != -1:  # Only consider if j can reach the end
                        max_jumps = max(max_jumps, 1 + dp[j])
            dp[i] = max_jumps

        return dp[0] if dp[0] != -1 else -1