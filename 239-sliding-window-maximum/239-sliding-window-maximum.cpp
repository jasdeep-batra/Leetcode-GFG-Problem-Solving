class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int i =0;
        int j =0;
        int sum = 0;
        int res = INT_MIN;
        list<int> maxi;
        vector<int> result;
        while(j<nums.size())
        {
            int it = maxi.size();
            while(it>0 && maxi.back() < nums[j])
            {
                maxi.pop_back();
                it--;
            }
            maxi.push_back(nums[j]);
            if(j-i+1 < k)
            {
                j++;
            }
            else
            {
                result.push_back(maxi.front());
                if(nums[i]==maxi.front())
                {
                    maxi.pop_front();
                }
                i++;
                j++;
            }
        }        
        return result;
    }
};