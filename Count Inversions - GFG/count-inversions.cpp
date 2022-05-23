// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution{
  public:
    long long int binarysearch(long long arr[], long long N, long long int first, long long int last)
    {
      long long int count =0;
        if(first<last)
        {
        int mid = (first+last)/2;
        count+=binarysearch(arr,N,first,mid);
        count+=binarysearch(arr,N,mid+1,last);
        count+=merge(arr,first,last,mid);
        }
        return count;
    }
    long long int merge(long long arr[], long long int first, long long int last, long long int mid)
    {
        long long int i = first,j=mid+1;long long int cnt=0;
        vector<long long int> temp;
        while(i<=mid && j<=last)
        {
            if(arr[i]>arr[j])
            {
                cnt+=(mid-i+1);
                temp.push_back(arr[j]);
                j++;
            }
            else{
                temp.push_back(arr[i]);
                i++;
            }
        }
        while(i<=mid)
        {
            temp.push_back(arr[i]);i++;
        }
        while(j<=last)
        {
            temp.push_back(arr[j]);j++;
        }
        long long ii=0;
        for(int g = first;g<=last;g++)
        {
            arr[g] = temp[ii];
            ii++;
        }
        return cnt;
    }
    long long int inversionCount(long long arr[], long long N)
    {
        // Your Code Here
        long long int fcount = binarysearch(arr,N,0,N-1);
        return fcount;
    }

};

// { Driver Code Starts.

int main() {
    
    long long T;
    cin >> T;
    
    while(T--){
        long long N;
        cin >> N;
        
        long long A[N];
        for(long long i = 0;i<N;i++){
            cin >> A[i];
        }
        Solution obj;
        cout << obj.inversionCount(A,N) << endl;
    }
    
    return 0;
}
  // } Driver Code Ends