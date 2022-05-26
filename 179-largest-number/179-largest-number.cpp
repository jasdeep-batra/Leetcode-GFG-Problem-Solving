class Solution {
public:
    string atoi(int num)
    {
        string res;
        while(num>0)
        {
            res+=((num%10)+'0');
            num/=10;
        }
        reverse(res.begin(),res.end());
        return res;
    }
    string largestNumber(vector<int>& nums) {
        vector<string> vt;
        for(auto i: nums)
        {
            string c = "0";
            if(i!=0) c = atoi(i);
            vt.push_back(c);
        }
        //sort(vt.begin(),vt.end(),greater<string>());
        // for(auto vv:vt)
        // {
        //     cout<<"\n"<<vv;
        // }
        // string res = vt[0];
        // for(int i=1;i<vt.size();i++)
        // {
        //     string c1 = vt[i] + res;
        //     string c2 = res +vt[i];
        //     if(stoi(c1)>stoi(c2))
        //     {
        //         res = vt[i] + res;
        //     }
        //     else{
        //         res = res + vt[i];
        //     }            
        // }
        sort(vt.begin(),vt.end(),[](string& s1, string& s3){return s1+s3>s3+s1;});
        string res;
        for(int i=0;i<vt.size();i++)
        {
                res+=vt[i];
        }
        while(res[0]=='0' && res.length()>1)
            res.erase(0,1);
        return res;
    }
};