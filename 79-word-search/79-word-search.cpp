class Solution {
public:
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int k)
    {        
        if(k==word.size())return true;
        if(i<0||j<0||i>=board.size()||j>=board[0].size()||board[i][j]!=word[k])return false;
        char c = board[i][j];
        board[i][j] = '*';
        bool get = dfs(board,word,i+1,j,k+1) || dfs(board,word,i-1,j,k+1) || dfs(board,word,i,j+1,k+1) || dfs(board,word,i,j-1,k+1);
        board[i][j] = c;
        return get;
    }
    bool exist(vector<vector<char>>& board, string word) {
        for(int i=0;i<board.size();i++)
        {
            for(int j=0;j<board[0].size();j++)
            {
                if(board[i][j]==word[0])
                {
                   if(dfs(board,word,i,j,0))
                   {
                       return true;
                   }
                }
            }
        }
        return false;
    }
};