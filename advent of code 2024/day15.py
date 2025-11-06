# Day 15 - Robot in Warehouse (Part 1 + Part 2)
# Compact, safe, dynamic, and error-free

path = r"C:\Users\EC\Downloads\the maps\vinegar\knowledge-skill and trade\discord bot\currency + map\advent of code 2024\day15.txt"

with open(path, "r") as f:
    raw = f.read().strip().split("\n")

# Split map/moves dynamically
split_idx = next(i for i, line in enumerate(raw) if not line.strip())
base_map = [list(r) for r in raw[:split_idx]]
moves = ''.join(raw[split_idx+1:]).replace('\n', '')

dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

# --- Helper: find robot ---
def find_robot(g):
    for r, row in enumerate(g):
        if '@' in row:
            return (r, row.index('@'))
    return (0, 0)

# --- Movement logic (works for both parts) ---
def move_robot(grid, robot, dr, dc):
    r, c = robot
    nr, nc = r + dr, c + dc
    if grid[nr][nc] == '#': return robot  # wall blocks

    # Collect chain of boxes
    chain = []
    while grid[nr][nc] in ('O', '[', ']'):
        chain.append((nr, nc))
        nr += dr
        nc += dc
        if grid[nr][nc] == '#': return robot  # wall blocks

    if grid[nr][nc] == '.':
        while chain:
            tr, tc = chain.pop()
            grid[tr + dr][tc + dc] = grid[tr][tc]
            grid[tr][tc] = '.'
        grid[r][c], grid[r + dr][c + dc] = '.', '@'
        return (r + dr, c + dc)
    return robot

# --- GPS Calculation ---
def gps_sum(grid, box_chars=('O', '[')):
    return sum(r * 100 + c for r, row in enumerate(grid) for c, val in enumerate(row) if val in box_chars)

# --- Run simulation ---
def simulate(g):
    robot = find_robot(g)
    for m in moves:
        robot = move_robot(g, robot, *dirs[m])
    return gps_sum(g)

# --- Part 1 ---
grid1 = [row[:] for row in base_map]
print("Part 1 GPS Sum:", simulate(grid1))

# --- Part 2: Expand map ---
expand = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
grid2 = [list(''.join(expand.get(ch, ch) for ch in row)) for row in base_map]
print("Part 2 GPS Sum:", simulate(grid2))
