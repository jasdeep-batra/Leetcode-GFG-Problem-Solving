class Solution {
public:
    vector<vector<string>> result;
    bool issafe(int i, int j, vector<string>& board)
    {
        for(int k = i-1;k>=0;k--)
        {
            if(board[k][j]=='Q')return false;
        }
        for(int k = j-1;k>=0;k--)
        {
            if(board[i][k]=='Q')return false;
        }
        for(int m=i,n=j; m>=0&&n>=0;m--,n--)
        {
            if(board[m][n]=='Q')return false;
        }
        for(int m=i,n=j; m<board.size()&&n>=0;m++,n--)
        {
            if(board[m][n]=='Q')return false;
        }
        return true;
    }
    void recursion(int col,vector<string>& board)
    {
        //base condition
        if(col==board.size())
        {
            result.push_back(board);
            return;
        }
        for(int i=0;i<board.size();i++)
        {
            if(issafe(i,col,board))
            {
                board[i][col] = 'Q';
                recursion(col+1,board);
                board[i][col] = '.';
            }
        }
        return;
    }
    vector<vector<string>> solveNQueens(int n) {
        string s;
        for(int i=0;i<n;i++)
        {
            s+='.';
        }
        
        vector<string> board(n,s);
        recursion(0,board);
        return result;        
    }
};