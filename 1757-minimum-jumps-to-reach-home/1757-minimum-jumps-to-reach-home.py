from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_set = set(forbidden)
        max_limit = max(max(forbidden),x) + a + b
        visited = set()
        queue = deque([(0,False)])  # (pos, steps, was_back)
        visited.add((0, False))
        steps = 0
        for pos in forbidden:
            visited.add((pos,False))
            visited.add((pos,True))
        while queue:
            for _ in range(len(queue)):
                pos, is_fw = queue.popleft()
                if pos == x:
                    return steps
                forward,backward = (pos+a,True), (pos-b,False)
                if pos+a <= max_limit and forward not in visited:
                    visited.add(forward)
                    queue.append(forward)
                if is_fw   and pos-b>0 and backward not in visited:
                    visited.add(backward)
                    queue.append(backward)
            steps+=1

            
        
        return -1