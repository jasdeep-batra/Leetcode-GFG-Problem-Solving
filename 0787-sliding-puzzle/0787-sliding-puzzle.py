class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # state
        #if (board[0]==[] and board[1]==[]):
        #(1,2,3,4,5,0)
        queue = deque()
        init_state =tuple(board[0]+board[1])
        final_state = tuple([1,2,3,4,5,0])

        queue.append((init_state,0))
        visit = set()
        visit.add(init_state)
        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        while queue:
            curr_state,step = queue.popleft()
            if curr_state == final_state:
                return step
            zero_index = curr_state.index(0)
            row,col = zero_index//3, zero_index%3
            for dx,dy in dirs:
                x,y = row+dx, col+dy
                if x>=0 and x<2 and y>=0 and y<3:
                    #we have to swap the value of x,y with row,col
                    curr_list = list(curr_state)
                    curr_list[zero_index],curr_list[3*x+y] = curr_list[3*x+y],curr_list[zero_index]
                    nextt = tuple(curr_list)
                    if nextt not in visit:
                        queue.append((nextt,step+1))
                        visit.add(nextt)

        return -1



            

