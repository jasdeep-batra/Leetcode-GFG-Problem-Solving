class Solution {
public:
    int maxDivide(int x,int y)
    {
        while(x%y==0)
        {
            x=x/y;
        }
        return x;
    }
    int isUgly(int no)
{
        if(no==0)return false;
    no = maxDivide(no, 2);
    no = maxDivide(no, 3);
    no = maxDivide(no, 5);
  
    return (no == 1) ? 1 : 0;
}
};