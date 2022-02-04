// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{

  public:
	int minDifference(int arr[], int n)  { 
	    int sum = 0;
	    for(int i=0;i<n;i++)
	    {
	        sum+=arr[i];
	    }
	    vector<vector<bool>> dp(n+1,vector<bool>(sum+1,false));
	    for(int i=0;i<n+1;i++)
	    {
	        dp[i][0] = true;
	    }
	    for(int i=1;i<n+1;i++)
	    {
	        for(int j=1;j<sum+1;j++)
    	    {
    	        if(j>=arr[i-1])
    	        {
    	            dp[i][j] = dp[i-1][j-arr[i-1]] || dp[i-1][j];
    	        }
    	        else
    	        {
    	            dp[i][j] = dp[i-1][j];
    	        }
	        }
	    }
	   // for(int i=0;i<n+1;i++)
	   // {
	   //     for(int j=0;j<sum+1;j++)
    // 	    {
    // 	        cout<<dp[i][j]<<" ";
    // 	    }
    // 	    cout<<endl;
	   // }
	    vector<int> result;
	    int diff = sum;
	    for(int i=0;i<sum/2+1;i++)
	    {
	        if(dp[n][i]==true)
	        {
	            //cout<<i<<" ";
	            result.push_back(sum - 2*i);
	        }
	    }
	    return result[result.size()-1];
	} 
};


// { Driver Code Starts.
int main() 
{
   
   
   	int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

        int a[n];
        for(int i = 0; i < n; i++)
        	cin >> a[i];

       

	    Solution ob;
	    cout << ob.minDifference(a, n) << "\n";
	     
    }
    return 0;
}  // } Driver Code Ends