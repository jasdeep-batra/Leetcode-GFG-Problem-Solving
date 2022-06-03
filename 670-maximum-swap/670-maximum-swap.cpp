struct CustomCompare
{
    bool operator()(const pair<int,int>& lhs, const pair<int,int>& rhs)
    {
        if(lhs.first==rhs.first)return lhs.second > rhs.second;
        return lhs.first < rhs.first;
    }
};
class Solution {
public:
    int maximumSwap(int num) {
        //comparator
        priority_queue<pair<int,int>> mp;
        vector<int> vt;
        int test = num, ii = 0;
        while(test>0)
        {
            vt.push_back(test%10);
            //mp[test%10] = ii;ii++;
            test/=10;
        }
        ii--;
        reverse(vt.begin(),vt.end());
        for(int i=0;i<vt.size();i++)
        {
            mp.push({vt[i],i});
        }
        for(int i=0;i<vt.size();i++)
        {
            cout<<vt[i]<<" "<<mp.top().first<<endl;
            if(vt[i]>=mp.top().first)
            {
                continue;
            }
            else if(vt[i]<mp.top().first && mp.top().second > i)
            {
                swap(vt[i],vt[mp.top().second]);
                break;
            }
            else if(i>mp.top().second)
            {
                i--;
                mp.pop();
            }            
        }
        int ans = 0;
        for(auto i: vt)
        {
            ans = ans*10 + i;
        }
        return ans;
    }
};