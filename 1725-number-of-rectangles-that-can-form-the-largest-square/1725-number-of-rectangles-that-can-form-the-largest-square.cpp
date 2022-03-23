class Solution {
public:    
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        unordered_map<int,int> mp;
        for(auto i: rectangles)
        {
            mp[min(i[0],i[1])]++;
        }
        int side = INT_MIN, res = INT_MIN;
        for(auto itr: mp)
        {
            if(itr.first>side){res = itr.second;side = itr.first;}
        }
        return res;
    }
};