// { Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
/*You are required to complete this function*/

class Solution{
    public:
    int maxLen(vector<int>&A, int n)
    {   
        map<int,int> mp;
        int sum =0,result=0;
        priority_queue<int> pq;
        for(int i=0;i<n;i++)
        {
            sum+= A[i];
            if(sum==0)
            {
                result = i+1;
                
            }
            else
            {   if(mp.find(sum)!=mp.end())
                {
                    int len = i - mp[sum];
                    result = max(result,len);
                    //cout<<"if working:"<<sum<<": "<<i<<endl;
                    
                }
                else
                {
                    //cout<<"else working:"<<i<<": "<<mp[sum]<<endl;
                    mp.insert(make_pair(sum,i));
                }
                
            }
        }
        //cout<<pq.top()<<endl;
        return result;
    }
};


// { Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int m;
        cin>>m;
        vector<int> array1(m);
        for (int i = 0; i < m; ++i){
            cin>>array1[i];
        }
        Solution ob;
        cout<<ob.maxLen(array1,m)<<endl;
    }
    return 0; 
}


  // } Driver Code Ends