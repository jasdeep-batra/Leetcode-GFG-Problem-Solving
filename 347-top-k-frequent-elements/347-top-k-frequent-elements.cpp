class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        sort(nums.begin(),nums.end());
        int i=0,j=1;
        priority_queue<pair<int,int>> pq;
        while(j<nums.size())
        {
            if(nums[j]==nums[i])
            {
                j++;
            }
            else
            {
                pq.push({j-i,nums[i]});
                i = j;
            }            
        }
        pq.push({j-i,nums[i]});
        while(k>0)
        {
            res.push_back(pq.top().second);
            pq.pop();
            k--;
        }
        return res;
    }
};