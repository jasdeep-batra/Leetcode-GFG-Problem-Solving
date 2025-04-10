class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            curx,cury = intervals[i]
            prevx, prevy = res[-1]
            if curx > prevy:
                res.append([curx,cury])
            else:
                res[-1] = [min(curx,prevx),max(cury,prevy)]

        return res





        