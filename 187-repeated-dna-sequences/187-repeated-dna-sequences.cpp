class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        //brute force method 
        unordered_map<string,int> mp;
        int range = s.size()-9;
        for(int i=0;i<range;i++)
        {
            string ss = s.substr(i,10);  // flag
            mp[ss]++;
        }
        vector<string> result;
        for(auto i: mp)
        {
            if(i.second>1)
            {
                result.push_back(i.first);
            }
        }
        return result;        
    }
};