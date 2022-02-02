class Solution {
public:
    
    string convertToTitle(int cno) {
        map<int,char> mp;
        char i ='A';
        int count = 1;
        while(i<='Z')
        {
            mp[count++] = i++;
        }
        string res;
        while(cno > 0)
        {
            int rem = cno%26;
            if(rem==0){
                res+='Z';
                cno = cno/26 - 1;
            }
            else {res+=mp[rem];
            cno = cno/26;}
        }
        cout<<res;
        reverse(res.begin(),res.end());
        return res;
    }
};