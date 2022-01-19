// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution
{
    public:
    vector<vector<int>> result;
    void recur(vector<int> arr, int itr, vector<int> res)
    {
        result.push_back(res);
        for(int i=itr;i<arr.size();i++)
        {
            if(i!=itr && arr[i]==arr[i-1])continue;
            res.push_back(arr[i]);
           // cout<<"res: "<<arr[i]<<" "<<i<<endl;
            recur(arr,i+1,res);
            res.pop_back();
        }
    }
    vector<vector<int> > AllSubsets(vector<int> arr, int n)
    {
        sort(arr.begin(),arr.end());
        vector<int> res;
        recur(arr,0,res);
        return result;
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> A;
        int x;
        for(int i=0;i<n;i++){
            cin>>x;
            A.push_back(x);
        }
        Solution obj;
        vector<vector<int> > result = obj.AllSubsets(A,n);
        // printing the output
        for(int i=0;i<result.size();i++){
            cout<<'(';
            for(int j=0;j<result[i].size();j++){
                cout<<result[i][j];
                if(j<result[i].size()-1)
                    cout<<" ";
            }
            cout<<")";
        }
        cout<<"\n";
    }
}   


  // } Driver Code Ends