// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
	public:
		int LongestRepeatingSubsequence(string str){
		    vector<vector<int>> dp(str.size()+1,vector<int>(str.size()+1,0));
		    for(int i=1;i<str.size()+1;i++)
		    {
		        for(int j=1;j<str.size()+1;j++)
		        {
		           if(str[i-1]==str[j-1] && i!=j)
		           {
		               dp[i][j] = 1+dp[i-1][j-1];
		           }
		           else
		           {
		               dp[i][j] = max(dp[i][j-1],dp[i-1][j]);
		           }
		        }
		    }
		    int ans = dp[str.size()][str.size()];
		    return ans;
		}

};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		string str;
		cin >> str;
		Solution obj;
		int ans = obj.LongestRepeatingSubsequence(str);
		cout << ans << "\n";
	}
	return 0;
}  // } Driver Code Ends