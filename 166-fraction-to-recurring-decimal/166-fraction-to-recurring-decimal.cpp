class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        char sign = '-';
        string num;
        if((numerator>0 && denominator<0) || (numerator<0 && denominator>0))num+=sign;
        long a = abs((long)numerator);
        long b = abs((long)denominator);
        long c = a/b;
        long long int rem = a%b;
        num += to_string(c);
        if(rem==0)return num;
        num+='.';
        map<long long int,int> mp;
        while(rem)
        {
            if(mp.find(rem)!=mp.end())
            {
                string mid = to_string(rem);
                num.push_back(')');
                num.insert(mp[rem],"(");
                break;
            }
            mp[rem] = num.size();
            rem = rem*10;
            int got = rem/b;
            string g = to_string(got);
            num+=g;
            rem = rem%b;
        }
        return num;
    }
};