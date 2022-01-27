// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

vector<long long> printFirstNegativeInteger(long long int arr[],
                                             long long int n, long long int k);

// Driver program to test above functions
int main() {
    long long int t, i;
    cin >> t;
    while (t--) {
        long long int n;
        cin >> n;
        long long int arr[n];
        for (i = 0; i < n; i++) {
            cin >> arr[i];
        }
        long long int k;
        cin >> k;

        vector<long long> ans = printFirstNegativeInteger(arr, n, k);
        for (auto it : ans) cout << it << " ";
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends



vector<long long> printFirstNegativeInteger(long long int A[],
                                             long long int N, long long int K) {
        
        long long int i =0;
        long long int j = 0;
        list<int> neg;
        vector<long long> result;
        while(j<N)
        {
            if(A[j]<0)
            {
                neg.push_back(A[j]);
            }
            if(j-i+1 < K)
            {
                j++;
            }
            else
            {
                if(neg.empty())result.push_back(0);
                else
                { 
                    result.push_back(neg.front());
                    if(A[i]==neg.front())
                    {
                        neg.pop_front();
                    }
                }
                i++;
                j++;
            }
        }
        return result;
                                                 
 }