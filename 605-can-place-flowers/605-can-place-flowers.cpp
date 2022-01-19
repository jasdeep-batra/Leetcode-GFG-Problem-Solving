class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int i=0,count=0;
        while(i<flowerbed.size())
        {
            if(flowerbed[i]==0)
            {
                int prev =1;int next =1;
                if(i==0 || flowerbed[i-1]==0)
                {
                    prev = 0;
                }
                if(i==flowerbed.size()-1 || flowerbed[i+1]==0 )
                {
                    next = 0;
                }
                if(prev==0 && next==0)
                {
                    flowerbed[i] = 1;
                    count++;
                }
            }
            i++;
        }
        if(count>=n)return true;
        return false;
    }
};