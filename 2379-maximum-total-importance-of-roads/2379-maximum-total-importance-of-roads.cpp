class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        //brute force
        vector<int> edge(n,0);
        priority_queue<pair<int,int>> pq; //count, node

        for(auto i: roads)
        {
            edge[i[0]]++;
            edge[i[1]]++;
        }
        long long ans = 0;
        sort(edge.rbegin(),edge.rend());
        for(long long i: edge)
        {
            if (i==0)
            {
                break;
            }
            long long geet = i;
            long long geet2 = n*i;
            ans+=geet2;
            n--;

        }
        return ans;
    }
};