class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        #upper bound problem
        left = min(batteries)
        right = sum(batteries)//n
        def canRun(charge):
            time = 0
            for bat in batteries:
                time+=min(charge,bat)

            return time
        ans = 0
        while right >= left:
            mid = (right+left)>>1
            if canRun(mid) >= mid*n:

                ans = mid
                left = mid+1
            else:
                right = mid-1

        return ans