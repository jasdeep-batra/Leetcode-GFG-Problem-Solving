class Solution {
    public int largestCombination(int[] candidates) {
        //we have to find the lenght of larget  subset such that it is postitive
        // till it is positive let it be 
        int max_ans = 0;
        for(int i=0;i<=24;i++)
        {
            int count_set = 0;
            int curr_index = 1<<i;
            for(int j=0;j<candidates.length;j++)
            {
                int current = candidates[j];
                
                if((current&curr_index)!=0)
                {
                    count_set+=1;
                }
            }
            max_ans = Math.max(max_ans,count_set);
        }
        return  max_ans;

    }
}