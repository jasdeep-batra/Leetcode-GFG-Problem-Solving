class Solution {
public:
    bool isPalindrome(string s) {
        string nospace;
        stringstream ss(s);
        string wrd;
        while(ss>>wrd)
        {
            nospace+=wrd;
        }
        string clean;
        map<char,char>mp;
        for(int i='A',j='a';i<='Z'&&j<='z';i++,j++)
        {
            mp[i]=j;
        }
        string res;
        for(int i=0;i<nospace.size();i++)
        {
            if(nospace[i]>='A'&&nospace[i]<'Z' || nospace[i]>='0' && nospace[i]<='9' ||nospace[i]>='a'&&nospace[i]<'z')
            {
                if(mp.find(nospace[i])!=mp.end()){
                    nospace[i] = mp[nospace[i]];
                }
                res+=nospace[i];
            }
        }
        string rres = res;
        reverse(rres.begin(),rres.end());
        //cout<<res<<" "<<rres;
        return rres==res;
    }
};