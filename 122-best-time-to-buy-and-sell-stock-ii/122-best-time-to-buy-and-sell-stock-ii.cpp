class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cur_pos = 0,prof_pos = 0,ans = 0,res=0;
        for(int i=1;i<prices.size();i++)
        {
            prof_pos = prices[i]-prices[i-1];
            if(prof_pos>0)ans+=prof_pos;
            cur_pos +=prof_pos;
            cur_pos = max(cur_pos,0);
            res = max(res,cur_pos);            
        }
        return max(res,ans);
    }
};