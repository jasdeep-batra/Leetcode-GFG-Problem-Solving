class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        map<char,int> lmp,rmp;
        vector<string> res;
        for(int g=0;g<words.size();g++)
        {
            bool tr1=true,tr2=true;
            for(int i=0;i<words[g].size();i++)
            {
                if(lmp.find(words[g][i])!=lmp.end() && lmp[words[g][i]]!=pattern[i])
                {
                    tr1 = false;
                    break;
                }
                lmp[words[g][i]] = pattern[i];
            }
            for(int i=0;i<words[g].size();i++)
            {
                if(rmp.find(pattern[i])!=rmp.end() && rmp[pattern[i]]!=words[g][i])
                {
                    tr2 = false;
                    break;
                }
                rmp[pattern[i]] = words[g][i];
            }
            if(tr1 && tr2)res.push_back(words[g]);
            lmp.clear();
            rmp.clear();
        }
        return res;
    }
};