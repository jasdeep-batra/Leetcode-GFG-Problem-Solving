class Solution {
public:
    int appendCharacters(string s, string t) {
        int i = 0;
        int j = 0;
        while((i< s.size()) &&  (j < t.size()))
        {
            while(i<s.size() && s[i]!=t[j])
            {
                i++;
            }
            if(s[i]==t[j])
            {
                j++;
                i++;
            }
            // cout<<i<<" : "<<j <<endl;
        }
        if(i>=s.size())
        {
            return t.size()-j;
        }
        return 0;
    }
};