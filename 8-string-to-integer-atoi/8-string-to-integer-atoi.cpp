
class Solution {
public:
    int myAtoi(string s) {
        string new_s;int m=0,n=s.size()-1;
        long ang=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]!=' ')
            {
                m = i;
                break;
            }
        }
        for(int i=s.size()-1;i>=0;i--)
        {
            if(s[i]!=' ')
            {
                n = i;
                break;
            }
        }
        new_s = s.substr(m,n-m+1);
        string ans;int flag = 1;
        for(int i=0;i<new_s.size();i++)
        {
            if((new_s[i]>='a' && new_s[i]<='z') || new_s[i]=='.')
            {
                break;
            }
            if(new_s[i]=='+' && ans.empty())
            {
                ans+=s[i];
                continue;// flag 1 means negative
            }
            if(new_s[i]==' ')break;
            if(new_s[i]=='-' && ans.empty())
            {
                ans+=s[i];
                flag = -1;
                continue;// flag 1 means negative
            }
            else if((new_s[i]=='-'|| new_s[i]=='+') && !(ans.empty()))
            {
                cout<<"works";
                break;
            }
            else {
                char cc = new_s[i];
                long dfg = cc-'0';cout<<dfg<<endl;
                ang = dfg + ang*10;
                cout<<flag<<endl;
                ans+=new_s[i];
                if(flag==1 && ang > INT_MAX)return INT_MAX;
                if(flag==-1 && -1*ang < INT_MIN)return INT_MIN;
            }
        }
        if(ans.empty()||ang==0)return 0;
        if(flag==-1 && (ang*flag) < INT_MIN)return INT_MIN;
        if(flag==1 && ang*flag > INT_MAX)return INT_MAX;
        //int anse = stoi(ans);
        return ang*flag;
    }
};
    
