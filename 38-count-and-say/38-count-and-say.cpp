class Solution {
public:
    string countAndSay(int n) {
        string s;
        s+='1';
        for(int i=2;i<=n;i++)
        {
            int count = 0;
            int j=0,k = 0;
            string r;
            while(k < s.size()) // 1
            {
                //cout<<"count: "<<count<<endl;
                if(s[j]==s[k])
                {
                    count++;
                    k++;
                }
                else{
                    char c = count+'0';
                    r+=c;
                    r+=s[j];
                    j=k;
                    count = 0;
                    //cout<<"check: "<<i<<" "<<r<<endl;
                }
            }
            
                r+=(count+'0');
                r+=s[j];
               // cout<<"check out: "<<i<<" "<<r<<endl;
            
            s = r;
            
        }
        return s;
    }
};