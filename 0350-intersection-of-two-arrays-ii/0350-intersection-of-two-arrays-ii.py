class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        new_dict2 = Counter(nums2)
        ans = []
        for i in nums1:
            if i in new_dict2 and new_dict2[i]!=0:
                ans.append(i)
                new_dict2[i]-=1

        return ans


        