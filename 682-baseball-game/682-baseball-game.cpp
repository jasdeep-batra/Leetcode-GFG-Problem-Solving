class Solution {
public:
    // int si(string s)
    // {
    //     int ans = 0;
    //     int flag = 1;
    //     for(int i=0;i<s.size();i++)
    //     {
    //         if(s[i]=='-')
    //         {
    //             flag = -1;
    //             continue;
    //         }
    //         int a = s[i]-'0';
    //         cout<<"a: "<<a<<endl;
    //         ans = ans*10;
    //         ans+=a;            
    //     }
    //     return ans*flag;
    // }
    int calPoints(vector<string>& ops) {
       // int score =0;
        //stack<int> st;
        vector<int> score;
        for(int i=0;i<ops.size();i++)
        {
            if(ops[i]=="+")
            {
                int ii = score.size()-1;
                int jj = score.size()-2;
                score.push_back(score[ii]+score[jj]);
            }
            else if(ops[i]=="C")
            {
                score.pop_back();
            }
            else if(ops[i]=="D")
            {
                score.push_back(score.back()*2);
            }
            else
            {
                //int s = si(ops[i]);
               // int sc = stoi(s);
                score.push_back(stoi(ops[i]));
            }            
        }
        int sum = accumulate(score.begin(),score.end(),0);
        return sum;
    }
};