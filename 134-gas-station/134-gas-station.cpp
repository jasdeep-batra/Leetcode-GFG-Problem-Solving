class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int i = 0;
        int n = gas.size();
        int fuel = 0,count = 0;
        int sum1=0,sum2=0;
        for(int j=0;j<n;j++)
        {
            sum1+=gas[j];
            sum2+=cost[j];
        }
        if(sum2>sum1)return -1;
        int ans = 0;
        while(i<n)
        {
            fuel += gas[i] - cost[i];
            if(fuel<0)
            {
                fuel = 0;
                ans = i+1;
            }
            i++;
        }
        if(fuel>=0)return ans;
        return -1;
    }
};