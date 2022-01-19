// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution{
public:
    vector<string> result;
    char space = ' ';
    void recur(string s, string res, int i)
    {
        if(i==s.size())
        {
            result.push_back(res);
            return;
        }
        recur(s,res+s[i],i+1);
        recur(s,res+space+s[i],i+1);
        
    }
    vector<string> permutation(string S)
    {
        string res;
        res+=S[0];
        recur(S,res,1);
        reverse(result.begin(),result.end());
        return result;
    }
};

// { Driver Code Starts.

int  main(){
    int t;
    cin>>t;
    while(t--){
        string S;
        cin>>S;
        vector<string> ans;
        Solution obj;
        ans = obj.permutation(S);
        for(int i=0;i<ans.size();i++){
            cout<<"("<<ans[i]<<")";
        }
        cout << endl;
    }
}
  // } Driver Code Ends