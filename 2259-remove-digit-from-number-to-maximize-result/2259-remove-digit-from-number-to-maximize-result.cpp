class Solution {
public:
    string removeDigit(string number, char digit) {
        int count = 0;
        vector<int> index;
        for(int i =0;i<number.size();i++)
        {
            if(number[i]==digit)
            {
                index.push_back(i);
            }
        }
        string ans = "00";
        for(int i=0;i<index.size();i++)
        {
            string temp = number;
            temp.erase(temp.begin()+index[i]);
            if(ans<temp)
            {
                ans = temp;
            }
        }
        return ans;
    }
};