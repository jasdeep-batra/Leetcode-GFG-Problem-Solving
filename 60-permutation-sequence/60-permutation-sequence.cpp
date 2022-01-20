class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> nums;
        int fact = 1;
        for(int i=1;i<=n;i++)
        {
            fact = fact*i;
            nums.push_back(i); 
        }
        fact/=n;
        string s;
        k = k-1;
        while(true)
        {
            char c = nums[k/fact] + '0';
            s += c;
            nums.erase(nums.begin()+(k/fact));
            if(nums.size()==0)
            {
                break;
            }
            k= k%fact;
            fact = fact/nums.size();
        }
        return s;
    }
};