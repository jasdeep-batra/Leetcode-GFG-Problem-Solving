class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        //naive approach
        vector<string> res;
        map<string,int> mp;
        map<int,set<string>> fin;
        //priority_queue<pair<int,string>> pq;
        for(auto i: words)
        {
            mp[i]++;
        }
        for(auto i: mp)
        {
            fin[i.second].insert(i.first);
            //pq.push({i.second,i.first});
        }
        for(auto itr = fin.rbegin(); itr!=fin.rend();itr++)
        {
                cout<<"work\n";
                //set<string> st = itr->second;
                for(auto btr: itr->second)
                {
                    if(res.size()!=k)
                    {
                        res.push_back(btr);                        
                    }
                    else
                    {
                        break;
                    }
                }
            
        }
        //reverse(res.begin(),res.end());
        return res;
    }
};