class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # h = endy - start y 
        # w = endx - start x
        # 1,5 0,2
        forx = [[sx,ex] for sx,sy,ex,ey in rectangles]
        fory = [[sy,ey] for sx,sy,ex,ey in rectangles]
        forx.sort()
        fory.sort()
        def calculate(arr):
            arr.sort()
            # print(arr)
            end = arr[0][1]
            cnt = 0
            for i in range(1,len(arr)):
                cx,cy = arr[i][0],arr[i][1]
                if cx >= end:
                    cnt+=1
                    end = cy
                else:
                    end = max(end,cy)
            # print(cnt)
            return True if cnt>=2 else False
        return calculate(forx) or calculate(fory)



        