class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        left = 1
        i = 1
        while i < len(arr):
            if arr[i] > arr[i-1]:
                left+=1
            else:
                break
            i+=1
        right = len(arr)
        j = len(arr)-2
        while j >=0:
            if arr[j] > arr[j+1]:
                right-=1
            else:
                break
            j-=1
        # print()
        return left == right and left > 1 and left < len(arr)  
        