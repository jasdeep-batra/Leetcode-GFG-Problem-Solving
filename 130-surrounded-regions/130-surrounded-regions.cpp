class Solution {
public:
    void recur(vector<vector<char>>& board, int i, int j)
    {
        if(i<0 || j<0 ||i==board.size()||j==board[0].size())return;
        if(board[i][j]=='X' || board[i][j]=='V')return;
        board[i][j] = 'V';
        recur(board,i-1,j);
        recur(board,i+1,j);
        recur(board,i,j-1);
        recur(board,i,j+1);
    }
    void solve(vector<vector<char>>& board) {
        for(int i=0;i<board.size();i++)
        {
            if(board[i][0]=='O')
            {
                recur(board,i,0);
            }
            if(board[i][board[0].size()-1]=='O')
            {
                recur(board,i,board[0].size()-1);
            }
        }
        for(int i=0;i<board[0].size();i++)
        {
            if(board[0][i]=='O')
            {
                recur(board,0,i);
            }
            if(board[board.size()-1][i]=='O')
            {
                recur(board,board.size()-1,i);
            }
        }
        for(int i=0;i<board.size();i++)
        {
            for(int j=0;j<board[0].size();j++)
            {
                if(board[i][j]=='V')board[i][j] = 'O';
                else board[i][j] = 'X';
            }
        }
    }
};