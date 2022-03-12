class Solution {
public:
    vector<int> partitionLabels(string s) {
        map<char,int> mp;vector<int> result;
        for(int i=0;i<s.size();i++)
        {
            mp[s[i]] = i;
        }
        int i=0,j=mp[s[i]];
        int start =0,end = j;
        while(i<s.size() && j<s.size())
        {
            if(i<j && mp[s[i]] <= j)
            {
                i++;
            }
            if(i==j)
            {
                result.push_back(end-start+1);
                //cout<<"working"<<endl;
                start = j+1;
                i++;
                j = mp[s[i]];
                end = mp[s[i]];
            }
            if(i<j && mp[s[i]] > j)
            {
                j = mp[s[i]];
                end = j;
            }            
        }
        return result;
    }
};