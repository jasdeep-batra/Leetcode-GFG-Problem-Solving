class Solution {
public:
    int myAtoi(string s) {
        if(s.size()==0)return 0;
        long ans=0;
        int ind = 0;
        int flag = 1;
        while(ind<s.size() && s[ind]==' ')
        {
            ++ind;
        }
        if(ind<s.size() && s[ind]=='-' || s[ind]=='+')
        {
            s[ind]=='-'? flag=-1: flag=1;
            ++ind;
        }
        for(int i=ind;i<s.size() && isdigit(s[i]);i++)
        {
            ans = ans*10 + (s[i] -'0');
            if(flag==-1 && -1*ans < INT_MIN)return INT_MIN;
            if(flag==1 && ans > INT_MAX)return INT_MAX;
        }
        return int(flag*ans);
    }
};