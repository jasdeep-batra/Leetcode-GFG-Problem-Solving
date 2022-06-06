class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int j = INT_MAX,k=INT_MAX; // k>j
        for(auto i:nums)
        {
            if(j>=i)
            {
                j = i;
            }
            else if(k>=i)
            {
                k = i;
            }
            else return true;
        }
        return false;
    }
};