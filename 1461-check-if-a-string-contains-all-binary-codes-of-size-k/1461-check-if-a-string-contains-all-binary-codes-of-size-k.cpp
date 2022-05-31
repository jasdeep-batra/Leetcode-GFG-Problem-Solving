class Solution {
public:
    bool hasAllCodes(string s, int k) {
        unordered_map<string,int> mp;
        //cout<<i<<endl;
        int size = s.size()-k;
        //cout<<size<<endl;
        for(int i=0;i<=size;i++)
        {
            //cout<<"working";
            string ss = s.substr(i,k);
            mp[ss]++;
        }
        int siz = pow(2,k);
        if(mp.size()>=siz)
        {
            return true;
        }
        return false;
    }
};