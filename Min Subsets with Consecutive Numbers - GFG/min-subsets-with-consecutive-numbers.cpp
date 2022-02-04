// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
    public:
    int numofsubset(int arr[], int n)
    {
        sort(arr,arr+n);
        int i =1, j =0, count = 1;
        while(i<n)
        {
            if(arr[i]==arr[i-1]+1)
            {
                i++;
            }
            else
            {
                count++;
                i++;
            }
        }
        return count;
    }
};

// { Driver Code Starts.
// Driven Program
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int arr[n+1];
	    for(int i=0; i<n; i++)
	        cin>>arr[i];
        Solution ob;
	    cout << ob.numofsubset(arr, n) << endl;
	}
	return 0;
}
  // } Driver Code Ends