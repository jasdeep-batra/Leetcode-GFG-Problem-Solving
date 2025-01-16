class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x = 0
        if len(nums1)%2==0 and len(nums2)%2==0:
            return 0
        elif len(nums1)%2!=0 and len(nums2)%2==0:
            for num in nums2:
                x ^= num
        elif len(nums1)%2==0 and len(nums2)%2!=0:
            for num in nums1:
                x ^= num
        else:
            for num in nums2:
                x ^= num
            for num in nums1:
                x ^= num

        return x