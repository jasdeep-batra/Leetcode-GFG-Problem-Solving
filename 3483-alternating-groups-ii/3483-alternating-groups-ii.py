class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        #we need to jump i to j if [j+1]==[j]
        n = len(colors)
        i,j=0,1
        ans = 0
        colors = colors+colors
        while(i<n):
            if (j-i+1)<=k:
                if (colors[j]!=colors[j-1]):
                    j+=1
                else:
                    i=j
                    j+=1
            else:
                ans+=1
                i+=1
                if colors[i]==colors[i-1]:
                    j = i+1

        return ans




        