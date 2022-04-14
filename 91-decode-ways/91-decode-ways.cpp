class Solution {
public:
    void mapping()
    {
        map<char,int> mp;
        int id = 1;
        for(char c = 'A'; c<='Z';c++)
        {
            mp[c] = id++;
        }
    }
    vector<int> mem;
    int partition(string s,int i)
    {
        //base case
        if(i==s.size())return 1;
        if(mem[i]!=-1)return mem[i];
        int ans = 0;
        if(s[i]!='0')ans+=partition(s,i+1);
        if(i+1<s.size() && (s[i]=='1' || s[i]=='2' && s[i+1]<='6'))ans+=partition(s,i+2);
        return mem[i]=ans;
    }
    int numDecodings(string s) {
        //dynamic programming or backtracking we might have to make the partitions
        mem.resize(1000,-1);
        return partition(s,0);
    }
};