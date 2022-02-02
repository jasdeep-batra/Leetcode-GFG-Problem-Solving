class Solution {
public:
    string countAndSay(int n) {
        string s;
        s+='1';
        for(int i=2;i<=n;i++)
        {
            //int count = 0;
            int j=0,k = 0;
            string r;
            while(k < s.size())
            {
                if(s[j]==s[k])
                {
                    //count++;
                    k++;
                }
                else{
                    char c = (k-j)+'0';
                    r+=c;
                    r+=s[j];
                    j=k;
                    //count = 0;
                }
            }
            
                r+=((k-j)+'0');
                r+=s[j];
            s = r;
            
        }
        return s;
    }
};