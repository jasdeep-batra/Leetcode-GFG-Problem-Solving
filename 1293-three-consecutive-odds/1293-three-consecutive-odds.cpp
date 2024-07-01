class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int c = 0;
        for(auto i: arr)
        {
            if(i%2!=0)
            {
                c++;
            }
            else{
                c=0;
            }
            if(c==3)return true;

        }
        return false;
    }
};