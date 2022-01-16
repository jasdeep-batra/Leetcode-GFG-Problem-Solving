// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Item{
    int value;
    int weight;
};


 // } Driver Code Ends
//class implemented
/*
struct Item{
    int value;
    int weight;
};
*/


class Solution
{
    public:
    //Function to get the maximum total value in the knapsack.
    double fractionalKnapsack(int W, Item arr[], int n)
    {
        vector<pair<double,int>> vt;
        for(int i =0;i<n;i++)
        {
            double frac = (arr[i].value*1.0)/(arr[i].weight*1.0);
            vt.push_back(make_pair(frac,arr[i].weight));
        }
        
        sort(vt.begin(),vt.end());
        reverse(vt.begin(),vt.end());
        //for(auto itr: vt)cout<<itr.first<<endl;
        int j = 0;double profit=0;
        for(int i=0;i<n;i++)
        {
            //if(j==0)break;
            if(W>vt[i].second+j)
            {
                profit += vt[i].first*vt[i].second;
                //cout<<"j"<<j<<endl;
                j=j+vt[i].second;
            }
            else
            {
                double x = (W-j)*1.0;
                profit += vt[i].first*x;
                break;
            }
            
        }
        return profit;
    }
        
};


// { Driver Code Starts.
int main()
{
	int t;
	//taking testcases
	cin>>t;
	cout<<setprecision(2)<<fixed;
	while(t--){
	    //size of array and weight
		int n, W;
		cin>>n>>W;
		
		Item arr[n];
		//value and weight of each item
		for(int i=0;i<n;i++){
			cin>>arr[i].value>>arr[i].weight;
		}
		
		//function call
		Solution ob;
		cout<<ob.fractionalKnapsack(W, arr, n)<<endl;
	}
    return 0;
}  // } Driver Code Ends