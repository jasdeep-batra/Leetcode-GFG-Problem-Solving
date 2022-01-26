class Solution {
public:
    bool check_day(vector<int> weight,int mid, int day)
    {
        int cnt = 1,i=0;
        int wght = mid;
        cout<<"mid: "<<mid<<endl;
        while(i<weight.size())
        {
            
            if(wght >= weight[i])
            {
                wght = wght - weight[i];
                i++;
            }
            else{
                cnt++;
                wght = mid;
            }
        }
        cout<<"count: "<<cnt<<endl;
        if(cnt<=day)return true;
        return false;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int max_weight = INT_MIN,sum=0;
        int ans = -1;
        for(int i=0;i<weights.size();i++)
        {
            sum+=weights[i];
            max_weight = max(max_weight,weights[i]);
        }
        int first = max_weight;
        int last = sum;
        while(last >= first)
        {
            int mid = first + (last-first)/2; // current ship capacity
            if(check_day(weights,mid,days)==true)
            {
               cout<<"wroing"<<endl;
                ans = mid;
                last = mid-1;
            }
            else{
               // cout<<"working"<<endl;
                first = mid+1;
            }            
        }
        return ans;
    }
};