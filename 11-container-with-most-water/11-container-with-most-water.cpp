class Solution {
public:
    int maxArea(vector<int>& height) {
        //ngr ngl
        int i = 0, j =height.size()-1, wl=0,wr=height.size()-1;
        int lmax = height[i];
        int rmax = height[j],ans=0;
        while(j>i)
        {
            lmax = height[i];
            rmax = height[j];
            int h = min(lmax,rmax);
            int w = j-i;
            ans = max(ans,h*w);
            if(lmax<rmax)
            {
                i++;
            }
            else
            {
                j--;
            }
        }
        return ans;
    }
};