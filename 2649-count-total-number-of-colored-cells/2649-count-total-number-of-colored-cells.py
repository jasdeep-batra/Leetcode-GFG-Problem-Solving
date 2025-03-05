class Solution:
    def coloredCells(self, n: int) -> int:
        # 1, 5, 13, 
        # 4,8,12,
        start = 1
        const = 4
        for i in range(1,n):
            start+=const
            const+=4
            # print(start," : ", const)

        return start
            


        