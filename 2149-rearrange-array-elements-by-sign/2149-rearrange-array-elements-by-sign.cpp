class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> help,res;
        int positive_end,negative_start;
        for(auto i: nums)if(i>0)help.push_back(i);
        positive_end = help.size();negative_start = help.size();
        for(auto i: nums)if(i<0)help.push_back(i);
        ///////////////////////////////////////
        int i = 0, j = negative_start;
        int k = 0;
        while(k<nums.size())
        {
            if(!(k&1)){
                res.push_back(help[i++]);
            }
            else res.push_back(help[j++]);
            k++;
        }
        return res;
    }
};