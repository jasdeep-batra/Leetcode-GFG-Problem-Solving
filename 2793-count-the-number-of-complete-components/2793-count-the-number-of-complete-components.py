class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        #union find
        parent = [i for i in range(n)]
        rank = [0]*n
        def find(node):
            if node!=parent[node]:
                parent[node]=find(parent[node])
            return parent[node]

        def union(vo,vt):
            po = find(vo)
            pt = find(vt)
            if po==pt:
                return 
            if rank[po]>rank[pt]:
                parent[pt] = po
            elif rank[po] < rank[pt]:
                parent[po] = pt
            else:
                parent[pt] = po
                rank[po]+=1
        
        for u,v in edges:
            union(u,v)
        
        vertices = defaultdict(set)
        edge = defaultdict(int)

        for i in range(n):
            rootn = find(i)
            vertices[rootn].add(i)

        for u,v in edges:
            root = find(u)
            edge[root]+=1

        ans = 0
        for root in vertices:
            vno = len(vertices[root])
            eno = edge[root]
            expected = vno * (vno-1)//2

            if expected==eno:
                ans+=1
        return ans



        