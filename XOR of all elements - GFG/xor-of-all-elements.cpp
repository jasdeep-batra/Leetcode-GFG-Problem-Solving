// { Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

 // } Driver Code Ends
class Solution
{
public:
    vector<int> getXor(vector<int> A, int N)
    {
        vector<int> result;
        int ans = 0;
        for(int j=0;j<N;j++)
        {
            ans = ans^A[j];
        }
        for(int i=0;i<N;i++)
        {
            int fans = ans^A[i];   
            result.push_back(fans);
        }
        return result;
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin >> N ;
        vector<int> A(N);

        for (int i = 0; i < N; i++)
        {
            cin >> A[i];
        }

        Solution ob;
        vector<int> B = ob.getXor(A, N);
        for(int i = 0 ; i < N ; i++)
        {
            cout << B[i] <<" ";
        }
        cout << endl;
    }
    return 0;
}  // } Driver Code Ends