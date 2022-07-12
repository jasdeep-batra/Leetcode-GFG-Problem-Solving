// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
  public:
    int shortestUnSub(string S, string T) {
        // code here
        vector<vector<int>> dp(S.size()+1,vector<int>(T.size()+1,1000));
        //f//or(int i=1;i<S.size()+1;i++)dp[i][0] = 1;
        //or(int i=1;i<T.size()+1;i++)dp[0][i] = 1;
        //dp[0][0] =0;
        for(int i=1;i<S.size()+1;i++)
        {
            for(int j=1;j<T.size()+1;j++)
            {
                int k = j;
                while(k && S[i-1]!=T[k-1])k--;
                if(k==0)dp[i][j]  =1;
                else dp[i][j] = min(dp[i-1][j],1+ dp[i-1][k-1]);
        
            }
        }
        // for(int i=0;i<S.size()+1;i++)
        // {
        //     for(int j=0;j<T.size()+1;j++)
        //     {
        //         cout<<dp[i][j]<<" ";
        //     }
        //     cout<<endl;
        // }
        int ans = dp[S.size()][T.size()];
        return (ans==1000)?-1:ans;
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string S,T;
        cin>>S>>T;

        Solution ob;
        cout << ob.shortestUnSub(S,T) << endl;
    }
    return 0;
}  // } Driver Code Ends