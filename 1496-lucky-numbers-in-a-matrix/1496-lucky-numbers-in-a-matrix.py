class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in matrix:
            minn = min(i)
            ind = i.index(minn)
            # print(minn,ind)
            maxx = -1
            for ii in range(len(matrix)):
                # print("df",matrix[ii][ind])
                maxx = max(maxx,matrix[ii][ind])
            # print(maxx)
            if maxx==minn:
                ans.append(minn)
        return ans

        