class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:  
        #looks like a graph...
        dictt = {}
        color = {}
        count = 0
        res = []
        k = 0
        for x,y in queries:
            if x in color:
                clr = color[x]
                dictt[clr]-=1
                if dictt[clr]==0:
                    dictt.pop(clr)
            color[x] = y

            if y not in dictt:
                dictt[y] = 1
            else:
                dictt[y] +=1
            res.append(len(dictt))
        return res




        