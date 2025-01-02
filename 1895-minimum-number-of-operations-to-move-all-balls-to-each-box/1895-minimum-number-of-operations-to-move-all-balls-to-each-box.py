class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0]*n
        for i in range(n):
            for j in range(n):
                if i!=j and boxes[j]=='1':
                    res[i]+=abs(i-j)

        print(res)
        return res

                    


        