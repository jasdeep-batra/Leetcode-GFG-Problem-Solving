class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev_end = intervals[0][1]
        prev_start = intervals[0][0] 
        res = [[prev_start,prev_end]]
        for i in range(1,len(intervals)):
            s,e = intervals[i]
            if prev_end >= s >= prev_start:
                res[-1][1] = max(prev_end,e)
                prev_end = max(prev_end,e)

            elif s > prev_end:
                res.append([s,e])
                prev_end = e
                prev_start = s


        return res


