// { Driver Code Starts
// C++ program to find minimum swaps required
// to club all elements less than or equals
// to k together
#include <bits/stdc++.h>
using namespace std;



 // } Driver Code Ends


class Solution
{
public:
    int minSwap(int arr[], int n, int k) {
        // Complet the function
        int ws = 0,ans=INT_MAX;
        for(int i=0;i<n;i++)
        {
            if(arr[i]<=k)ws++;
        }
        int in = 0;//  include 
        for(int i=0;i<n;i++)
        {
            if(i<ws)
            {
                if(arr[i]<=k)
                {
                    in++;
                }
            }
            else{
                if(arr[i]<=k)in++;
                if(arr[i-ws]<=k && in>0)in--;
            }
            ans = min(ans,ws-in);
        }
        return ans;
    }
};


// { Driver Code Starts.

// Driver code
int main() {

	int t,n,k;
	cin>>t;
	while(t--)
    {
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++)
            cin>>arr[i];
        cin>>k;
        Solution ob;
        cout << ob.minSwap(arr, n, k) << "\n";
    }
	return 0;
}
  // } Driver Code Ends