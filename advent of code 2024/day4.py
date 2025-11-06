# Advent of Code 2024 - Day 4: Ceres Search

import os

path = r"C:\Users\EC\Downloads\the maps\vinegar\knowledge-skill and trade\discord bot\currency + map\advent of code 2024\day4.txt"

with open(path, "r") as file:
    data = file.read().strip()

grid = [list(line.strip()) for line in data.splitlines()]
rows, cols = len(grid), len(grid[0])

# ---------------- Part 1 ---------------- #
word = "XMAS"
directions = [
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1),   # right
    (-1, -1), # up-left
    (-1, 1),  # up-right
    (1, -1),  # down-left
    (1, 1)    # down-right
]

def in_bounds(r, c):
    return 0 <= r < rows and 0 <= c < cols

part1_count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == word[0]:
            for dr, dc in directions:
                match = True
                for i in range(len(word)):
                    nr, nc = r + dr * i, c + dc * i
                    if not in_bounds(nr, nc) or grid[nr][nc] != word[i]:
                        match = False
                        break
                if match:
                    part1_count += 1

print("Part 1 — Total XMAS occurrences:", part1_count)


#Part 2

part2_count = 0

for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        if grid[r][c] == 'A':  # center of the X
            # Diagonal 1 (↘ or ↙)
            diag1 = grid[r - 1][c - 1] + 'A' + grid[r + 1][c + 1]
            diag2 = grid[r - 1][c + 1] + 'A' + grid[r + 1][c - 1]
            
            # Check both diagonals are "MAS" or "SAM"
            valid_diag1 = diag1 in ("MAS", "SAM")
            valid_diag2 = diag2 in ("MAS", "SAM")
            
            if valid_diag1 and valid_diag2:
                part2_count += 1

print("Part 2 — Total X-MAS (cross patterns):", part2_count)
