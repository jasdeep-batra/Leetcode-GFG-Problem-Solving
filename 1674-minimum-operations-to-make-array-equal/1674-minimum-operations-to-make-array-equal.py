class Solution:
    def minOperations(self, n: int) -> int:
        net = 1,3,5,7,9,11
        ind,mid =0,0
        if n%2!=0:
            ind = n//2
            mid = 2*ind+1
        else:
            ind = n//2
            mid = (2*ind+1 + 2*(ind-1)+1)//2
        ind-=1
        ans=0
        while ind>=0:
            curr = 2*ind+1
            ans+=(mid-curr)
            ind-=1


        
        return ans


        