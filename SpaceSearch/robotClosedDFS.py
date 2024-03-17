def is_valid_move(x, y, closed_positions):
    if (x, y) in closed_positions:
        return False
    if x < 1 or y < 1 or x > 4 or y > 5:
        return False
    return True

def dfs(robot_x, robot_y, target_x, target_y, closed_positions, path):
    if robot_x == target_x and robot_y == target_y:
        return True
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    for dx, dy in directions:
        new_x, new_y = robot_x + dx, robot_y + dy
        if is_valid_move(new_x, new_y, closed_positions) and (new_x, new_y) not in path:
            path.append((new_x, new_y))
            print("Exploring:", new_x, new_y)
            if dfs(new_x, new_y, target_x, target_y, closed_positions, path):
                return True
            path.pop()  # Backtrack if the path is not valid
            print("Backtracking:", new_x, new_y)
    
    return False

# Define the closed positions
closed_positions = [(1, 1), (1, 2)]
#closed_positions = [(1, 1), (1, 2), (1, 4), (1, 5), (3, 2), (4, 2), (2, 4), (2, 5)]

# Set the initial position of the robot and the coffee location
robot_position = (1, 1)  # Robot's initial position
coffee_location = (5, 5)  # Coffee location

# Run DFS algorithm to find the path to the coffee location
path = [(1, 1)]  # Start from the initial position
if dfs(robot_position[0], robot_position[1], coffee_location[0], coffee_location[1], closed_positions, path):
    print("Path found to coffee:", path)
else:
    print("No path found to coffee.")
