class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int sum_diff = 0,res = 0;
        for(int i=1;i<prices.size();i++)
        {
            sum_diff += prices[i]-prices[i-1];
            sum_diff = max(sum_diff,0);
            res = max(res,sum_diff);
        }
        return res;
    }
};