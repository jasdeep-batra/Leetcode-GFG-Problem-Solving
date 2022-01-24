class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        int a =0;
        vector<int> result;
        for(int j =1;j<10;j++)
        {
            a = j;
            for(int i=j+1;i<10;i++)
            {
                a = a*10+i;
                if(a>=low && a<=high)
                {
                    result.push_back(a);
                } 
            }
                       
        }
        sort(result.begin(),result.end());
        return result;
            
        }        
};