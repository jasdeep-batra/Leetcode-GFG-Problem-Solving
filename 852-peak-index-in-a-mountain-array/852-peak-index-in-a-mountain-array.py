class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        f = 0
        l = len(arr)-1
        n = len(arr)
        while l >= f:
            mid = f + (l-f)//2
            if(mid>0 and mid<n-1):
                if(arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]):
                    return mid
                elif arr[mid-1] > arr[mid]:
                    l = mid-1
                elif arr[mid+1] > arr[mid]:
                    f = mid+1
            elif(mid==0):
                return mid+1
            elif(mid==n-1):
                return mid-1
                    
        return -1
        