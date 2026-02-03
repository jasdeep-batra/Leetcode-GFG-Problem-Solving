class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*10001
        stack = []
        for i in range(len(nums2)):
            if not stack:
                stack.append(i)

            while stack and nums2[i] > nums2[stack[-1]]:
                ind = stack.pop()
                ans[nums2[ind]] = nums2[i]

            stack.append(i)

        res = [ans[val] for val in nums1]
        return res 