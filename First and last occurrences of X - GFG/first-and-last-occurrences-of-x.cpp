// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
  public:
    vector<int> result;
    int firstoccur(vector<int> arr, int n, int x)
    {
        int fo = -1;
        int first = 0;
        int last = n-1;
        while(last>=first)
        {
            int mid = first + (last-first)/2;
            
            if(arr[mid]==x)
            {
                fo = mid;
                last = mid-1;
            }
            else if(x > arr[mid])
            {
                first = mid+1;
            }
            else last = mid-1;
        }
        return fo;
    }
    int lastoccur(vector<int> arr, int n, int x)
    {
        int fo = -1;
        int first = 0;
        int last = n-1;
        while(last>=first)
        {
            int mid = first + (last-first)/2;
            
            if(arr[mid]==x)
            {
                fo = mid;
                first = mid+1;
            }
            else if(x > arr[mid])
            {
                first = mid+1;
            }
            else last = mid-1;
        }
        return fo;
    }
    vector<int> firstAndLast(vector<int> &arr, int n, int x) {
        int fo = firstoccur(arr,n,x);
        int lo = lastoccur(arr,n,x);
        if(fo==-1)
        {
            result.push_back(-1);
            return result;
        }
        result = {fo,lo};
        return result;
    }
};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, x;
        cin >> n >> x;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        Solution obj;
        vector<int> ans= obj.firstAndLast(arr, n, x) ;
        for(int i:ans){
            cout<<i<<" ";
        }
        cout<< endl;
    }
    return 0;
}
  // } Driver Code Ends