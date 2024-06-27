class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        unordered_map<int,int> mp;
        for(auto i: edges){
            mp[i[0]]++;
            mp[i[1]]++;
        }
        for(auto i: mp)
        {
            if (i.second == mp.size()-1)
            {
                return i.first;
            }
        }
        return -1;
    }
};