// { Driver Code Starts
#include<bits/stdc++.h>
 
using namespace std;

int sumDiff(int S[], int n);

 
// Driver program to test above function
int main()
{
   int t;
   cin>>t;
   while(t--)
   {
   	int n;
   	cin>>n;
   	int S[n];
   	for(int i=0;i<n;i++)
   	cin>>S[i];
    cout<<sumDiff(S, n)<<endl;;
   }
  
    return 0;
}// } Driver Code Ends

int sumfirst(int s[], int n)
{
    int sum =0;
    for(int i=0;i<n;i++)
    {
        sum+=s[i]*pow(2,n-(i+1));
    }
    return sum;
}
int sumlast(int s[], int n)
{
    int sum =0;
    for(int i=0;i<n;i++)
    {
        sum+=s[i]*pow(2,i);
    }
    return sum;
}

int sumDiff(int s[], int n)
{
    int sf = sumfirst(s,n);
    int sl = sumlast(s,n);
    int res = sl-sf;
    return res;
}