// { Driver Code Starts
// CPP program to find maximum sum
// by selecting a element from n arrays
#include<bits/stdc++.h>

using namespace std;

// To calculate maximum sum by
// selecting element from each array
int maximumSum( int n,int m, vector<vector<int>> &a);



// Driver program to test maximumSum
int main() {
    int t,n,m;
    cin>>t;
    while(t--)
    {
        cin>>n>>m;
        vector<vector<int>> arr(n, vector<int>(m,0));
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            cin>>arr[i][j];
            
        cout << maximumSum(n,m,arr)<<endl;
    
    }
    return 0;

}
// } Driver Code Ends


int maximumSum( int n,int m, vector<vector<int>> &a) {
    for(int i=0;i<n;i++)
    {
        sort(a[i].begin(),a[i].end());
    }
    int sum=a[n-1][m-1];
    int lef = a[n-1][m-1];
    int count = 1;
    for(int i=n-1;i>0;i--)
    {
        //cout<<"i: "<<i<<"\n";
        int k = m-1,j=m-1;
        //cout<<"k: "<<k<<"\n";
        while(k>=0)
        {
            //cout<<"working\n";
            if(lef > a[i-1][k])
            {
                // cout<<"val: "<<a[i-1][k]<<endl;
                 
                sum+=(a[i-1][k]);
                lef = a[i-1][k];
                //cout<<"lef: "<<lef<<endl;
                count++;
                break;
            }
            else k--;
        }
        if(k<0)return 0;
    }
    //cout<<count<<" "<<sum<<endl;
    //if(count<n)return 0;
    return sum;
    
}