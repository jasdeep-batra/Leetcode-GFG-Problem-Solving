class Solution:
    def trap(self, height: List[int]) -> int:
        #monotonic stack 
        #updated version
        # two pointer appraoch 
        left = 1
        right = len(height)-2
        min_left = 0
        min_right = len(height)-1
        ans = 0
        while(right>=left):
            if height[min_right] >height[min_left]:
                if height[left] > height[min_left]:
                    min_left = left                
                else:
                    ans+=(height[min_left]-height[left])
                left+=1
            else:
                if height[right] > height[min_right]:
                    min_right = right                
                else:
                    ans+=(height[min_right]-height[right])
                right-=1
        return ans
            



        