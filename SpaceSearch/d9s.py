from itertools import permutations

def inversions(puzzle):
    inv_count = 0
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] and puzzle[j] and puzzle[i] > puzzle[j]:
                inv_count += 1
    return inv_count

def is_solvable(puzzle):
    inv_count = inversions(puzzle)
    return inv_count % 2 == 0

def generate_puzzles():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    permutations_list = permutations(numbers)
    puzzles = [puzzle for puzzle in permutations_list if is_solvable(puzzle)]
    return puzzles

# Generate solvable puzzles
solvable_puzzles = generate_puzzles()

print("Number of solvable initial states:", len(solvable_puzzles))
