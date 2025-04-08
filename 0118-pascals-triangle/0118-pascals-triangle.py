class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]

        ans = [[1],[1,1]]
        for i in range(3,numRows+1):
            temp = ans[-1]
            curr = []
            for i in range(len(temp)-1):
                curr.append(temp[i]+temp[i+1])
            temp = [1] + curr + [1]
            ans.append(temp)
        return ans

        