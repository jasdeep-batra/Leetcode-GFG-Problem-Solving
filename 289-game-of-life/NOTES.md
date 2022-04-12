(i>0 && board[t][j]==1)?count_zero++:count_one++;
(i<board.size()-1 && board[d][j]==1)?count_one++:count_zero++;
(j>0 && board[i][l]==1)?count_zero++:count_one++;
(j<board[0].size()-1 && board[i][r]==1)?count_one++:count_zero++;
((i>0&&j>0) && board[i-1][j-1]==1)?count_one++:count_zero++;
((i<board.size()-1 && j>0) && board[i+1][j-1]==1)?count_one++:count_zero++;
((i>0&&j<board[0].size()-1) && board[i-1][j+1]==1)?count_one++:count_zero++;
((i<board.size()-1&&j<board[0].size()-1) && board[i+1][j+1]==1)?count_one++:count_zero++;