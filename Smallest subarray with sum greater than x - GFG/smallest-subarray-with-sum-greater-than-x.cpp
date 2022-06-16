// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution{
  public:

    int smallestSubWithSum(int arr[], int n, int x)
    {
       int i=0,j=0,sum=arr[0],size=INT_MAX;
        while(j<n)
        {
            if(sum<=x)
            {
                j++;
                sum+=arr[j];
            }
            else{
                size = min(size,j-i+1);
                sum-=arr[i];
                i++;
                
            }
        }
        return size;
    }
};

// { Driver Code Starts.

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
		int n,x;
		cin>>n>>x;
		int a[n];
		for(int i=0;i<n;i++)
		cin>>a[i];
		Solution obj;
		cout<<obj.smallestSubWithSum(a,n,x)<<endl;
	}
	return 0;
}  // } Driver Code Ends