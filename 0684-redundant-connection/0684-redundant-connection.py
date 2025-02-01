
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [0]*1001
        parent = [i for i in range(1001)]
        def find(node):
            if parent[node]!=node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1,node2):
            p1 = find(node1)
            p2 = find(node2)
            if rank[p1]==rank[p2]:
                rank[p1]+=1
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1]+=1
            if rank[p2]<rank[p1]:
                parent[p1] = p2
                rank[p2]+=1
        x,y = -1,-1
        for i,j in edges:
            root1,root2 = find(i),find(j)
            if root1==root2:
                return [i,j]
            parent[root2] = root1
        return []

        


        