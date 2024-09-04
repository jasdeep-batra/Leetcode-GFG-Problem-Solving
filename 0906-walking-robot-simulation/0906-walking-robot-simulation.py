class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions represent (dx, dy) for north, east, south, west respectively.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # north, east, south, west
        dir_index = 0  # Start facing north
        
        # Convert obstacle list to a set of tuples for fast lookup
        obstacle_set = set(map(tuple, obstacles))
        
        curr_x, curr_y = 0, 0  # Robot's starting position
        max_distance = 0  # To track the maximum Euclidean distance squared
        
        for command in commands:
            if command == -2:  # Turn left
                dir_index = (dir_index - 1) % 4
            elif command == -1:  # Turn right
                dir_index = (dir_index + 1) % 4
            else:
                dx, dy = directions[dir_index]
                for _ in range(command):
                    next_x, next_y = curr_x + dx, curr_y + dy
                    if (next_x, next_y) not in obstacle_set:
                        curr_x, curr_y = next_x, next_y
                        max_distance = max(max_distance, curr_x**2 + curr_y**2)
                    else:
                        break  # Stop moving if there's an obstacle

        return max_distance
