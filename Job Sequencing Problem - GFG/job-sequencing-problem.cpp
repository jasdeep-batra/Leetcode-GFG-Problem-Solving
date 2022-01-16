// { Driver Code Starts
// Program to find the maximum profit job sequence from a given array 
// of jobs with deadlines and profits 
#include<bits/stdc++.h>
using namespace std; 

// A structure to represent a job 
struct Job 
{ 
    int id;	 // Job Id 
    int dead; // Deadline of job 
    int profit; // Profit if job is over before or on deadline 
}; 


 // } Driver Code Ends


class Solution 
{
    public:
    //Function to find the maximum profit and the number of jobs done.
    vector<int> JobScheduling(Job arr[], int n) 
    { 
        vector<pair<int,int>> vt;
        for(int i=0;i<n;i++)
        {
            vt.push_back(make_pair(arr[i].profit,arr[i].dead));
        }
        sort(vt.begin(),vt.end());
        reverse(vt.begin(),vt.end());
        int maxi = vt[0].second;
        for(int i=1;i<n;i++)
        {
            maxi = max(maxi,vt[i].second);
        }
        int arra[maxi+1];
        for(int i=0;i<maxi+1;i++)
        {
            arra[i] = -1;
        }
        //for(auto itr: vt) cout<<itr.first<<endl;
        int profit=0,job=0,i=0,j,deadd = 0;
        while(i<n)
        {
            deadd = vt[i].second;
            while(deadd>0)
            {
                if(arra[deadd]==-1)
                {
                    arra[deadd]=1;
                    profit+=vt[i].first;
                    //cout<<profit<<endl;
                    job++;
                    break;
                }
                deadd--;
            }
            i++;
        }
        vector<int> result;
        result = {job,profit};
        return result;
    } 
};



  // } Driver Code Ends

// { Driver Code Starts.
// Driver program to test methods 
int main() 
{ 
    int t;
    //testcases
    cin >> t;
    
    while(t--){
        int n;
        
        //size of array
        cin >> n;
        Job arr[n];
        
        //adding id, deadline, profit
        for(int i = 0;i<n;i++){
                int x, y, z;
                cin >> x >> y >> z;
                arr[i].id = x;
                arr[i].dead = y;
                arr[i].profit = z;
        }
        Solution ob;
        //function call
        vector<int> ans = ob.JobScheduling(arr, n);
        cout<<ans[0]<<" "<<ans[1]<<endl;
    }
	return 0; 
}


  // } Driver Code Ends