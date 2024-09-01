class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if len(original) < m*n or len(original) > m*n:
            return []

        for i in range(0,len(original),n):
            row = original[i:i+n]
            ans.append(row)
            #print(row)
        return ans



        