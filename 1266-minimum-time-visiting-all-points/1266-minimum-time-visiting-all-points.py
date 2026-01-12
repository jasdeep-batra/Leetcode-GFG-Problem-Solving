class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0
        for i in range(1,len(points)):
            pi,pj = points[i-1][0],points[i-1][1]
            ci,cj = points[i][0],points[i][1]
            ans+=max(abs(ci-pi),abs(cj-pj))
        return ans
