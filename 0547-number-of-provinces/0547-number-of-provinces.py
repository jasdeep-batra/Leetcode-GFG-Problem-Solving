class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]

        def find(node):
            if parent[node]!=node:
                parent[node] = find(parent[node])
            return parent[node]
        for i in range(len(isConnected)):
            for j in range(i+1,len(isConnected)):
                if isConnected[i][j]==1:
                    root_i = find(i)
                    root_j = find(j)
                    if root_i!=root_j:
                        parent[root_j] = root_i   
        print(parent)
        return len(set([find(i) for i in range(len(isConnected))]))


                




        
        
        