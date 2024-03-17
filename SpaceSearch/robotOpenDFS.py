import sys
def dfs(robot_position, coffee_position, visited, path):
    # Base case: If robot is at coffee position, return path
    if robot_position == coffee_position:
        return path
    
    # Explore adjacent cells
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x = robot_position[0] + dx
        new_y = robot_position[1] + dy
        
        # Check if new position is within bounds and not visited
        if 0 <= new_x < 4 and 0 <= new_y < 5 and (new_x, new_y) not in visited:
            visited.add((new_x, new_y))
            path.append((new_x, new_y))
            result = dfs((new_x, new_y), coffee_position, visited, path)
            
            # If coffee found, return path
            if result:
                return result
            
            # Backtrack if coffee not found
            path.pop()
            visited.remove((new_x, new_y))
    
    # If coffee not found in any direction
    return None

def find_coffee(robot_position, coffee_position):
    visited = set()
    visited.add(robot_position)
    path = [robot_position]
    return dfs(robot_position, coffee_position, visited, path)

# Example usage
robot_position = (1, 1)
#coffee_position = (sys.argv[1],sys.argv[2])  # Coffee position
#coffee_position = (3, 4)  # Coffee position
coffee_position = (2, 4)  # 
solution = find_coffee(robot_position, coffee_position)
print("Solution:", solution)
