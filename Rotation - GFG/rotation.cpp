// { Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


 // } Driver Code Ends
//User function template for C++
class Solution{
public:	
// int findKRotation(int arr[], int n) {
//     // code here
//     int low =0 , high = n-1; 
//       while(low<=high){
//           int mid = low + (high-low)/2 ; 
//           int prev = (mid-1 + n)  %n , next = (mid+1)%n ; //for corner cases like 

// //if first element is mid or last element is mid then simply use modulo 
//           if(arr[mid]<=arr[prev] && arr[mid]<=arr[next]) return mid;
//           else if (arr[mid]<=arr[high]) high = mid-1 ; 
//           else if (arr[mid]>=arr[low])  low=mid+1 ; 
//       }
//       return 0 ; 
// }
	int findKRotation(int arr[], int n) {
	    int first = 0;
	    int last = n-1;
	    while(last>=first)
        {
            int mid = (last+first)/2;
            int perv = (mid+n-1)%n;
            int next = (mid+1)%n;
            if((arr[mid] <= arr[perv]) && (arr[mid] <= arr[next]))
            {
                return mid;
            }
            else if(arr[mid] <= arr[last])
            {
                last = mid-1;
            }
            else if(arr[mid] >= arr[first])
            {
                first = mid+1;
            }
            
        }
        return 0;
	}

};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, i;
        cin >> n;
        int a[n];
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        auto ans = ob.findKRotation(a, n);
        cout << ans << "\n";
    }
    return 0;
}
  // } Driver Code Ends