class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        rank = [0]*n
        parent = [i for i in range(n)]
        countCycle = 0
        def find(node):
            if parent[node]!=node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            par1 = find(node1)
            par2 = find(node2)

            if (rank[par1]==rank[par2]):
                parent[par2] = par1
                rank[par1]+=1
            elif (rank[par1] > rank[par2]):
                parent[par2] = par1
            else:
                parent[par1] = par2

        # def isCycle(node1,node2):
        #     #to get the ultimate parent
        #     if find(node1)==find(node2):
        #         return True
        #     return False
        
        
        for i,j in connections:
            if find(i)==find(j):
                countCycle+=1
            union(i,j)
        for i in range(len(parent)):
            parent[i] = find(parent[i])
        # print(parent)
        # print(countCycle)
        unique = len(set(parent))
        if countCycle >= (unique-1):
            return unique-1
        return -1


            


          
        