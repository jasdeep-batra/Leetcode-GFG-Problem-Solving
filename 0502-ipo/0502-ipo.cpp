class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        //heap problem
        //knapsack problem
        //greedy problem
        //sorting
        int n = profits.size();  
        vector<pair<int,int>> store;
        for(int i=0;i<n;i++)
        {
            store.push_back({capital[i],profits[i]});
        }
        sort(store.begin(),store.end());
        priority_queue<int> pq;
        int j = 0;
        for(int i=0; i< k;i++)
        {
            while(j<n && store[j].first <= w)
            {
                pq.push(store[j].second);
                j++;
            }
            if(pq.empty())break;
            w+=pq.top();
            pq.pop();

        }
        return w;
    }
};