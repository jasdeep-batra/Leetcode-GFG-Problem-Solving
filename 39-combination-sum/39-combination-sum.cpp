class Solution {
public:
    vector<vector<int> > result;
    void recfun(vector<int> arr,int target, int n, vector<int> row)
    {
        for(int i = n;i>0;i--)
        {
            cout<<"target: "<<target<<endl;
            if(arr[i-1]==target)
            {
                cout<<"wroking"<<endl;
                row.push_back(arr[i-1]);
                result.push_back(row);
                row.pop_back();
                continue;
            }
            else if((target/arr[i-1])<1)
            {           
                cout<<"else if: "<<arr[i-1]<<endl;
                continue;
            }                   
            else
            {
                if((target/arr[i-1]) >= 1)
                {
                    cout<<"else (if): "<<arr[i-1]<<endl;
                    row.push_back(arr[i-1]);
                    recfun(arr,target-arr[i-1],i,row);
                    row.pop_back();
                }
                else{cout<<"else (else): "<<arr[i-1]<<endl;
                row.push_back(arr[i-1]);
                recfun(arr,target-arr[i-1],i-1,row);
                row.pop_back();}
                
            }
        }
        
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> row;
        recfun(candidates,target,candidates.size(),row);
        return result;
    }
};