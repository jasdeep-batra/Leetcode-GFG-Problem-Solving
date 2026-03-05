class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist)-1:
            return -1
        i,j = 1,10**7
        ans = -1
        def canCover(speed):
            hours = 0.0
            for d in range(len(dist)-1):
                hours+=math.ceil(dist[d]/speed)
            hours+=(dist[-1]/speed)
            return hours<=hour
        while j>i:
            mid = (i+j)//2
            if canCover(mid):
                ans = mid
                j = mid
            else:
                i = mid+1

        return i

