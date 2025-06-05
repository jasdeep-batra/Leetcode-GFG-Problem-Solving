class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        #it is a question of union find
        carr = [chr(i) for i in range(ord('a'),ord('z')+1)]
        print(carr)
        def find(char):
            if carr[ord(char)-ord('a')]!=char:
                carr[ord(char)-ord('a')] = find(carr[ord(char)-ord('a')])
            return carr[ord(char)-ord('a')]

        def union(chr1,chr2):
            par1 = find(chr1)
            par2 = find(chr2)

            if  par1!=par2:
                if ord(par1) < ord(par2):
                    carr[ord(par2)-ord('a')] = par1

                else:
                    carr[ord(par1)-ord('a')] = par2
        
        for i in range(len(s1)):
            union(s1[i],s2[i])
        ans = ""
        for item in baseStr:
            ans+=find(item)
        return ans





