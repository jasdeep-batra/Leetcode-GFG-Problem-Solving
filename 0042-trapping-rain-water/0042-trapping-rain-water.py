class Solution:
    def trap(self, height: List[int]) -> int:
        mx_i,i = 0,0
        n = len(height)
        mx_j,j = 0,n-1
        ans = 0
        while j>i:
            if height[i] < height[j]:
                mx_i = max(mx_i,height[i])
                ans+=(mx_i-height[i])
                i+=1
            else:
                mx_j = max(mx_j,height[j])
                ans+=(mx_j-height[j])
                j-=1

        return ans