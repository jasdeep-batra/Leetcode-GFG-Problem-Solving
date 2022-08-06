class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        stack<pair<int,int>> s;
        vector<pair<int,int>> pr;
        for(int i=0;i<speed.size();i++)
        {
            pr.push_back({position[i],speed[i]});
        }
        sort(pr.begin(),pr.end(),greater<>());
        for(auto i: pr)
        {
            if(s.empty())s.push({i.first,i.second});
            else{
                double time = (double)(target-s.top().first)/(double)s.top().second;
                double time2 = (double)(target-i.first)/(double)i.second;
                if(time<time2)
                {
                    s.push({i.first,i.second});
                }
            }
        }
        return s.size();
    }
};