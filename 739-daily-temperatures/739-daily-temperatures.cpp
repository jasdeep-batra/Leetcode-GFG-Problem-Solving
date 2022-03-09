class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
        stack<pair<int,int>> s;
        vector<int> ngr(temp.size(),0);
        for(int i=temp.size()-1;i>=0;i--)
        {
            
            while(!(s.empty()) && temp[i] >= s.top().first)
            {
                s.pop();
            }
            if(!(s.empty()) && s.top().first > temp[i])
            {
                ngr[i] = s.top().second - i;
            }
            s.push({temp[i],i});
        }
        return ngr;
    }
};