class mycomparator{
    public:
    bool operator()(pair<int,string>p1,pair<int,string>p2)
    {
        if(p1.first==p2.first)return p1.second<p2.second;
        return p1.first>p2.first;
    }
};
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        map<string,int> mp;
        vector<string> result;
        for(auto i: words)
        {
            mp[i]++;
        }
        
        priority_queue<pair<int,string>,vector<pair<int,string>>, mycomparator> pq;
        for(auto itr:mp)
        {
            pq.push({itr.second,itr.first});
            if(pq.size()>k)
            {
                pq.pop();
            }
        }
        while(!pq.empty())
        {
            result.push_back(pq.top().second);
            pq.pop();
        }
        reverse(result.begin(),result.end());
        return result;
    }
};