class Solution {
public:    
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        map<int,int> mp;
        for(auto i: rectangles)
        {
            int ans = min(i[0],i[1]);
            mp[ans]++;
        }
        auto itr = mp.rbegin();
        return itr->second;
    }
};