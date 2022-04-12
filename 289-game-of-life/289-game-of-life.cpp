class Solution {
public:
    int check_condition(vector<vector<int>>& board, int i, int j)
    {
        int count = 0;
        int t = i-1,d = i+1,l = j-1,r = j+1;
        if(t>=0 && board[t][j]==1)count++;
        if(d<board.size() && board[d][j]==1)count++;
        if(l>=0 && board[i][l]==1)count++;
        if(r<board[0].size() && board[i][r]==1)count++;
        if((t>=0&&l>=0) && board[t][l]==1)count++;
        if((t>=0&&r<board[0].size()) && board[t][r]==1)count++;
        if((d<board.size()&&l>=0) && board[d][l]==1)count++;
        if((d<board.size()&&r<board[0].size()) && board[d][r]==1)count++;
        return count;
    }
    void gameOfLife(vector<vector<int>>& board) {
        vector<vector<int>>ans = board; 
        for(int i=0;i<board.size();i++)
        {
            for(int j=0;j<board[0].size();j++)
            {
                int count = check_condition(ans,i,j);
                //cout<<count<<endl;
                if(board[i][j]==0)
                {
                    if(count==3)
                    {
                        board[i][j]=1;
                    }
                }
                if(board[i][j]==1)
                {
                    //cout<<res[1]<<endl;
                    if(count<2)
                    {
                        board[i][j]=0;
                    }
                    if(count==2 || count==3)
                    {
                        continue;
                    }
                    if(count>3)
                    {
                        board[i][j]=0;
                    }
                }
            }
        }
    }
};