class Solution {
public:
    string removeKdigits(string num, int k) {
        stack<char> s;
        string ans;
        s.push(num[0]);
        for(int i=1;i<num.size();i++)
        {
            while(k>0 && !s.empty() && s.top()>num[i])
            {
                s.pop();
                k--;
            }
            s.push(num[i]);
        }
        while(k && !s.empty())
        {
            s.pop();
            k--;
        }
        while(!s.empty())
        {
            ans+=s.top();s.pop();
        }
        reverse(ans.begin(),ans.end());
        while(ans[0]=='0' && ans.size()>1){
            ans.erase(ans.begin());
        }
        if(ans.empty())return "0";
        return ans;
    }
};