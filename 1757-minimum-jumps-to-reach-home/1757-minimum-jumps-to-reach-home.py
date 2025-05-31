from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_set = set(forbidden)
        max_limit =  10000
        visit = set()
        queue = deque([(0, 0, False)])  # (pos, steps, was_last_backward)
        visit.add((0, False))
        
        while queue:
            curr, step, back = queue.popleft()
            if curr == x:
                return step
            
            # Try both directions
            for jump in [a, -b]:
                if back and jump == -b:  # Skip backward if last was backward
                    continue
                
                new_pos = curr + jump
                new_back = jump == -b  # True if this is a backward jump
                
                if (0 <= new_pos <= max_limit and 
                    new_pos not in forbidden_set and 
                    (new_pos, new_back) not in visit):
                    visit.add((new_pos, new_back))
                    queue.append((new_pos, step+1, new_back))
        
        return -1