class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j = m,0
        while j<n:
            nums1[i] = nums2[j]
            i+=1
            j+=1
        nums1.sort()
        
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        