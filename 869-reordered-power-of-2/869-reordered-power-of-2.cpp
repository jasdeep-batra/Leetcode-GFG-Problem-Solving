class Solution {
public:
    string sort_the_digit(int n)
    {
        string num = to_string(n);
        sort(num.begin(),num.end());
        return num;
    }
    bool reorderedPowerOf2(int n) {
        for(int i=0;i<30;i++)
        {
            string sort_n = sort_the_digit(n);
            string sort_2 = sort_the_digit(pow(2,i));
            if(sort_n==sort_2)return true;
        }
        return false;
    }
};