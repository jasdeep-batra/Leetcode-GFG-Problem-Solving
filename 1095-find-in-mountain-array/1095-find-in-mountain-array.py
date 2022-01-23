# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def bs(self,f,l, mountain_arr: 'MountainArray',k):
        while l>=f:
            mid = f + (l-f)//2
            mide = mountain_arr.get(mid)
            if(mide==k):
                   return mid
            elif(mide > k):
                l = mid-1
            else:
                f = mid+1
        return -1
    
    def rbs(self,f,l,mountain_arr: 'MountainArray',k):
        while l>=f:
            mid = f + (l-f)//2
            mide = mountain_arr.get(mid)
            if(mide==k):
                   return mid
            elif(mide > k):
                f = mid+1
            else:
                l = mid-1
        return -1
        
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        f = 0
        l = mountain_arr.length()-1
        n = mountain_arr.length()
        ind = 0
        while l>=f:
            mid = f +(l-f)//2
            if(mid>0 and mid<n-1):
                mide = mountain_arr.get(mid)
                if(mide>mountain_arr.get(mid-1) and mide>mountain_arr.get(mid+1)):
                    ind = mid
                    break
                elif(mountain_arr.get(mid+1) > mide):
                    f = mid+1
                elif(mountain_arr.get(mid-1) > mide):
                    l = mid-1
            elif(mid==0):
                ind = mid+1
                break
            elif(mid==n-1):
                ind = mid-1
                break
        obj = Solution() 
        print(mid)
        fi = obj.bs(0,ind-1,mountain_arr,target)
        fj = obj.rbs(ind,n-1,mountain_arr,target)
        if(fi==-1 and fj==-1):
            return -1
        if(fi!=-1):
            return fi
        return fj
                    
                
        
        
        