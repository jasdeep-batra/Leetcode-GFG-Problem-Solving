class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        //brute force
        map<int,int> mp;
        vector<int> edge(n,0);
        priority_queue<pair<int,int>> pq; //count, node

        for(auto i: roads)
        {
            mp[i[0]]++;
            mp[i[1]]++;
        }
        for(auto i: mp)
        {
            pq.push({i.second,i.first});
        }
        long long ans = 0;
        for(long long i=n;i>=1;i--)
        {
            //edges * top number
            if(pq.empty())break;
            long long geet = pq.top().first;
            long long geet2 = geet*i;
            ans+=geet2;
            pq.pop();
        }
        return ans;
    }
};