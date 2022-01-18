class Solution {
public:
    vector<vector<int> > result;
    void recfun(vector<int> arr,int target, int i, vector<int> row)
    {
        if(i==0)
        {
                if(target==0)
                {
                    result.push_back(row);
                }
         return;
        }
            
                if(target>=arr[i-1]) 
                {
                    cout<<"else (if): "<<arr[i-1]<<endl;
                    row.push_back(arr[i-1]);
                    recfun(arr,target-arr[i-1],i,row);
                    row.pop_back();
                }               
                recfun(arr,target,i-1,row);
               
                
            
        
        
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> row;
        recfun(candidates,target,candidates.size(),row);
        return result;
    }
};