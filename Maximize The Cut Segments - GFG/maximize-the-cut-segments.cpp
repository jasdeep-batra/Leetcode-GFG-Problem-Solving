// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;



 // } Driver Code Ends


class Solution
{
    public:
    //Function to find the maximum number of cuts.
    int maximizeTheCuts(int n, int x, int y, int z)
    {
        vector<int> segment = {x,y,z};
        vector<vector<int>> dp(4,vector<int>(n+1,0));
        for(int i = 1;i<4;i++)
        {
            for(int j = 1;j<n+1;j++)
            {
                if(j>=segment[i-1] && (dp[i][j-segment[i-1]]!=0 || j==segment[i-1]))
                {
                    dp[i][j] = max(1 + dp[i][j-segment[i-1]], dp[i-1][j]);
                }
                else
                {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        int ans = dp[3][n];
        return ans;
    }
};

// { Driver Code Starts.
int main() {
    
    //taking testcases
    int t;
    cin >> t;
    while(t--)
    {
        //taking length of line segment
        int n;
        cin >> n;
        
        //taking types of segments
        int x,y,z;
        cin>>x>>y>>z;
        Solution obj;
        //calling function maximizeTheCuts()
        cout<<obj.maximizeTheCuts(n,x,y,z)<<endl;

    }

	return 0;
}  // } Driver Code Ends