class Solution {
public:
    vector<int> frequency(string s)
    {
        vector<int> freq(26,0);
        for(auto i: s)
        {
            freq[i-'a']++;
        }
        return freq;
    }
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        vector<int> max_freq_word2(26,0);
        for(auto j: words2)
        {
            vector<int> freq = frequency(j);
            for(int i=0;i<26;i++)
            {
                max_freq_word2[i] = max(max_freq_word2[i],freq[i]);
            }
        }
        vector<string> res;
        for(auto j:words1)
        {
            bool cant = false;
            vector<int> freq = frequency(j);
            for(int i=0;i<26;i++)
            {
                if(freq[i]<max_freq_word2[i]){
                    cant = true;
                    break;
                }
            }
            if(cant==false)res.push_back(j);
        }
        return res;
    }
};