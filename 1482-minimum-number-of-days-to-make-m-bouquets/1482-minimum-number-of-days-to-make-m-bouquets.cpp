class Solution {
public:
    bool check_flow(vector<int>& bloomDay, int m, int k, int mid)
    {
        int bc = 0; // bouqert created
        int day = mid; // 9
        int i=0;
        int kc = k;
        while(i<bloomDay.size())
        {
            if(day >= bloomDay[i] && kc!=0) //3 2 1
            {
                kc--;
                i++;
                if(kc==0){
                    bc++;
                    kc = k;
                }
            }
            
            else {
                kc = k;
                i++;
            }
            
        }   
        cout<<"bc: "<<bc<<endl;
        if(bc>=m)return true;
    return false;
    }
    int minDays(vector<int>& bloomDay, int m, int k) {
        if(m*k > bloomDay.size())return -1;
        int first = INT_MAX;
        int ans = -1;
        int last = 0;
        for(int i=0;i<bloomDay.size();i++)
        {
            last = max(last,bloomDay[i]);
            first = min(first,bloomDay[i]);
        }
        cout<<"first"<<last<<endl;
        while(first <=last)
        {
            int mid = first + (last-first)/2;
            cout<<"mid"<<mid<<endl;
            if(check_flow(bloomDay,m,k,mid))
            {
                ans = mid;
                last = mid-1;
            }
            else
            {
                first = mid+1;
            }
        }
        return ans;
    }
};