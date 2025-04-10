class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j =m-1,n-1
        k = n+m-1
        while(j>=0):
            if i>=0 and (nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i-=1
                k-=1
            else:
                nums1[k] = nums2[j]
                k-=1
                j-=1
        """
        Do not return anything, modify nums1 in-place instead.
        """
        