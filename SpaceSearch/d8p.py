from collections import deque

# Define the goal state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Define the possible moves
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def dfs(initial_state):
    visited = set()
    stack = deque([(initial_state, [])])

    while stack:
        state, path = stack.pop()

        if state == goal_state:
            return path

        visited.add(state)
        zero_index = state.index(0)

        for move in moves[zero_index]:
            new_state = list(state)
            new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
            new_state_tuple = tuple(new_state)
            if new_state_tuple not in visited:
                stack.append((new_state_tuple, path + [move]))
                print("Move:", move)

    return None

# Example usage
initial_state = (1, 2, 3, 4, 5, 0, 7, 8, 6)
solution = dfs(initial_state)
print("Solution:", solution)
