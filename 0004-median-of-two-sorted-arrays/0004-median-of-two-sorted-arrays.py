class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # do we need to use any time of sorting alogorithm
        k = len(nums1)+len(nums2)
        arr = [0]*k
        i,j = 0,0
        g = 0
        while i<len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr[g] = nums1[i]
                i+=1
            else:
                arr[g] = nums2[j]
                j+=1
            g+=1

        while i < len(nums1):
            arr[g] = nums1[i]
            i+=1
            g+=1
        
        while j < len(nums2):
            arr[g] = nums2[j]
            j+=1
            g+=1

        print(arr)
        if k%2==0:
            return (arr[k//2]+arr[(k//2)-1])/2

        return arr[k//2]