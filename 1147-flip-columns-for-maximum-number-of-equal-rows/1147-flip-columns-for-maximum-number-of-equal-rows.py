class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        dictt = defaultdict(int)

        for row in matrix:
            row_tuple = tuple(row)
            if row[0]==1:
                row_tuple = tuple([0 if i else 1 for i in row])

            dictt[row_tuple]+=1
        return max(dictt.values())



        

            





        