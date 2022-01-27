// { Driver Code Starts
// Initial template for C++

#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function template in C++

class Solution 
{
    public:
    bool check_page(int A[],int N,int mid, int M)
    {
        int stud_count = 1;
        int i=0;
        int pages = mid;
        while(i<N)
        {
            if(pages >= A[i])
            {
                pages = pages - A[i];
                i++;
            }
            else
            {
                stud_count++;
                pages = mid;
            }
        }
        if(stud_count <= M)return true;
        return false;
    }
    //Function to find minimum number of pages.
    int findPages(int A[], int N, int M) 
    {
        int first = INT_MIN;
        int last = 0;
        int ans = -1;
        for(int i=0;i<N;i++)
        {
            last+=A[i];
            first = max(first,A[i]);
        }
        while(first <= last)
        {
            int mid = first + (last-first)/2;
            if(check_page(A,N,mid,M))
            {
                ans = mid;
                last = mid-1;
            }
            else
            {
                first = mid+1;
            }
        }
        return ans;
        
    }
};

// { Driver Code Starts.

int main() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int A[n];
        for(int i=0;i<n;i++){
            cin>>A[i];
        }
        int m;
        cin>>m;
        Solution ob;
        cout << ob.findPages(A, n, m) << endl;
    }
    return 0;
}
  // } Driver Code Ends