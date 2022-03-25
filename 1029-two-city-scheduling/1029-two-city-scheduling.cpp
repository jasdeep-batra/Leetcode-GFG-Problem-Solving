class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        int a=0,b=0,i=0;vector<int> diff;
        int n = costs.size()/2;int cost=0;
        for(int i=0;i<costs.size();i++)
        {
            cost+=costs[i][0];
            diff.push_back(costs[i][1]-costs[i][0]);
        }
        sort(diff.begin(),diff.end());
        while(i<costs.size()/2)
        {          
            cost+=diff[i];
            i++;
        }
        return cost;
    }
};