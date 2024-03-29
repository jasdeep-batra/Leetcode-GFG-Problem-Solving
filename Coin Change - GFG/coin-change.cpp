// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
  public:
    long long int count(int S[], int size, int n) {
        vector<vector<long long int>> dp(size+1,vector<long long int>(n+1,0));
        for(int i=0;i<size+1;i++)
        {
            dp[i][0] = 1;
        }
        for(int i=1;i<size+1;i++)
        {
            for(int j=0;j<n+1;j++)
            {
                if(j>=S[i-1])
                {
                    dp[i][j] = dp[i][j-S[i-1]] +  dp[i-1][j];
                }
                else
                {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        long long int ans =  dp[size][n];
        return ans;
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        int arr[m];
        for (int i = 0; i < m; i++) cin >> arr[i];
        Solution ob;
        cout << ob.count(arr, m, n) << endl;
    }

    return 0;
}  // } Driver Code Ends