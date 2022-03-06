class Solution {
public:
    bool issubstring(string a, string b)
    {
        int siz = b.size();
        for(int i=0;i<=a.size()-siz;i++)
        {
            string s = a.substr(i,siz);            
            if(s==b)return true;
        }
        return false;
    }
    int repeatedStringMatch(string a, string b) {
            string na = a;int cnt = 1;
            while(na.size()<b.size())
            {
                na+=a;
                cnt++;
            }
            if(issubstring(na,b))return cnt;
            if(issubstring(na+na,b))return cnt+1;
        return -1;
    }
};