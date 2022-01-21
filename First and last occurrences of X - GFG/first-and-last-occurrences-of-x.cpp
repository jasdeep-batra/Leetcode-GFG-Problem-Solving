// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
  public:
    vector<int> res;
    int fo = 0;
    int lo = 0;
    int binaryl(int n,vector<int> arr,int first, int last, int x)
    {   
        if(last>=first){
            int mid = first + (last-first)/2;
            if((mid == 0 || x > arr[mid - 1]) && arr[mid] == x)
            {
                return mid;
            }
            else if (x > arr[mid])
                return binaryl(n,arr,mid+1,last,x);
            else
                return binaryl(n,arr,first,mid-1,x);
        }
        return -1;
    }
    int binaryr(int n, vector<int> arr,int first, int last, int x)
    {   
        if(last>=first){
            int mid = first + (last-first)/2;
            if((mid == n-1 || arr[mid+1]>x)&&arr[mid]==x)
            {
                return mid;
            }
            else if(x<arr[mid])
                return binaryr(n,arr,first,mid-1,x);
            else
                return binaryr(n,arr,(mid+1),last,x);
        }
        return -1;
    }
    vector<int> firstAndLast(vector<int> &arr, int n, int x) {
        fo = binaryl(n,arr,0,n-1,x);
        lo = binaryr(n,arr,0,n-1,x);
        vector<int> fr;
        if(fo==-1 && lo==-1) fr={-1};
        else fr = {fo,lo};
        return fr;
        
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