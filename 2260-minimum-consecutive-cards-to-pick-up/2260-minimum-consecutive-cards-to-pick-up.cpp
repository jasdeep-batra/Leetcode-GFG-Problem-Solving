class Solution {
public:
    int minimumCardPickup(vector<int>& cards) {
        map<int,int> mp;
        int dist = INT_MAX;
        for(int i=0;i<cards.size();i++)
        {
            if(mp.find(cards[i])!=mp.end())
            {
                dist = min(dist,i-mp[cards[i]]+1);
                mp[cards[i]] = i;
            }
            else
            {
                mp[cards[i]] = i;
            }
        }
        if(mp.size()==cards.size())return -1;
        return dist;
    }
};