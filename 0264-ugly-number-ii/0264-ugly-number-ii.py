class Solution:
    def nthUglyNumber(self, l: int) -> int:
        res = []
        res.append(1)
        m,n,o=1,1,1
        a,b,c=2,3,5
        for i in range(1,l):
            curr = min(a,min(b,c))
            res.append(curr)
        
            if curr==a:
                a = res[m]*2
                m+=1
            if curr==b:
                b = res[n]*3
                n+=1
            if curr==c:
                c = res[o]*5
                o+=1

        return res[-1]
            


        