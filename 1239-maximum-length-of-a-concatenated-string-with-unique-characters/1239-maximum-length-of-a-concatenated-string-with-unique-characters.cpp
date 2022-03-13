class Solution {
public:
    //vector<int>result;
    int result;
    Solution(){
        result = 0 ;
    }
    bool arediff(string s)
    {
        //if(a.size()==0 || b.size()==0)return true;
        //string s = a+b;
        map<char,int> mp;
        for(int i=0;i<s.size();i++)
        {
            if(mp.find(s[i])!=mp.end())
            {
                return false;
            }
            else
            {
                mp[s[i]] = 1;
            }
        }
        return true;        
    }
    void recursion(vector<string> arr, int i, string res)
    {
        if(arediff(res)==false)
        {
            return;
        }
        
        // if(i==arr.size())
        // {
        //     //cout<<"res: "<<res<<endl;
        //     //result.push_back(res.size());
        //     int siz = res.size();
        //     result = max(result,siz);
        //     return;
        // }
        int siz = res.size();
        result = max(result,siz);
        for(int ind = i;ind<arr.size();ind++)
        {
                //s+=arr[ind];
            recursion(arr,ind+1,res+arr[ind]);
            
        }        
    }
    int maxLength(vector<string>& arr) {
        string res;
        recursion(arr,0,res);
        //sort(result.begin(),result.end());
        // for(auto itr: result)
        // {
        //     cout<<itr<<endl;
        // }
        return result;
    }
};