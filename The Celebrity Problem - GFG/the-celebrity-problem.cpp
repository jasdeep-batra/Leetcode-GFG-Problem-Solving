// { Driver Code Starts
//Initial template for C++

#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++

class Solution 
{
    public:
    //Function to find if there is a celebrity in the party or not.
    int celebrity(vector<vector<int> >& M, int n) 
    {
        stack<int> s;
        for(int i=0;i<n;i++)
        {
            s.push(i);
        }
        int count = 0;
        
        while(s.size()!=1)
        {
            int p1 = s.top();
            s.pop();
            int p2 = s.top();
            s.pop();
            if(M[p1][p2] == 1)
            {
                s.push(p2);
            }
            else if(M[p2][p1]==1)
            {
                s.push(p1);
            }
        }
        int index = s.top();
        for(int i=0;i<n;i++)
        {
            if(M[index][i]==1)
            {
                return -1;
            }
            if(i!=index && M[i][index]==0)
            {
                return -1;
            }
        }
        return index;
    }
};

// { Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<vector<int> > M( n , vector<int> (n, 0));
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                cin>>M[i][j];
            }
        }
        Solution ob;
        cout<<ob.celebrity(M,n)<<endl;

    }
}
  // } Driver Code Ends