class Solution {
public:
    vector<int> result;
    void recursion(int num, int  n, int k)
    {
        //base condition
        if(n==1)
        {
            result.push_back(num);return;
        }
        if(num%10-k>=0)recursion(num*10+(num%10-k),n-1,k);
        if(k)if(num%10+k<10)recursion(num*10+(num%10+k),n-1,k);
    }
    vector<int> numsSameConsecDiff(int n, int k) {
        // vector<int> result;
        // for(int i=1;i<=9;i++)
        // {
        //     int j = n;
        //     int nn = i;
        //     bool flag = true;
        //     //cout<<nn;
        //     string num;
        //     num+=(nn+'0');
        //     for(int g=1;g<n;g++)
        //     {
        //         if(nn+k <10){ 
        //             nn+=k;
        //             num+=(nn+'0');
        //             //cout<<nn;
        //         }
        //         else if(nn-k>=0){
        //             nn-=k;
        //             num+=(nn+'0');
        //             //cout<<nn;
        //         }
        //         else{
        //             flag = false;
        //         }
        //     }
        //     if(num.size()==n){int number = stoi(num);
        //     result.push_back(number);}
        //     //cout<<endl;
        // }
        for(int i=1;i<=9;i++)
        {
            recursion(i,n,k);
        }
        return result;
    }
};