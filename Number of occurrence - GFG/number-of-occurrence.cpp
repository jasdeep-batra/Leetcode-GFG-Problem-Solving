// { Driver Code Starts


#include<bits/stdc++.h>

using namespace std;


 // } Driver Code Ends
//User function template for C++
class Solution{
public:	
	/* if x is present in arr[] then returns the count
		of occurrences of x, otherwise returns 0. */
	int first(int arr[], int n, int x)
	{
	    int first = 0;
	    int last = n-1;
	    int index = -1;
	    while(last>=first)
	    {
	        int mid = first + (last-first)/2;
	        if(arr[mid]==x)
	        {
	            index = mid;
	            last = mid-1;
	        }
	        else if(x>arr[mid])
	        {
	            first = mid+1;
	        }
	        else
	        {
	            last = mid-1;
	        }
	    }
	    return index;
	}
	int last(int arr[], int n, int x)
	{
	    int first = 0;
	    int last = n-1;
	    int index = -1;
	    while(last>=first)
	    {
	        int mid = first + (last-first)/2;
	        if(arr[mid]==x)
	        {
	            index = mid;
	            first = mid+1;
	        }
	        else if(x>arr[mid])
	        {
	            first = mid+1;
	        }
	        else
	        {
	            last = mid-1;
	        }
	    }
	    return index;
	}
	int count(int arr[], int n, int x) {
	    int f = first(arr,n,x);
	    int l = last(arr,n,x);
	    if(f==-1)return 0;
	    int ans = l-f+1;
	    return ans;
	}
};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, x;
        cin >> n >> x;
        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution ob;
        auto ans = ob.count(arr, n, x);
        cout << ans << "\n";
    }
    return 0;
}
  // } Driver Code Ends