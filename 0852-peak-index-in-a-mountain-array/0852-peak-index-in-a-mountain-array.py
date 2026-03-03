class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i,j = 0,len(arr)-1
        n = len(arr)
        while j>i:        
            mid = (i+j)//2
            if arr[mid] > arr[mid+1]:
                j = mid
            else:
                i = mid+1

        return i