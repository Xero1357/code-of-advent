# --- Load input file ---
path = r"C:\Users\EC\Downloads\the maps\vinegar\knowledge-skill and trade\discord bot\currency + map\advent of code 2024\day6.txt"

with open(path, "r") as file:
    lines = [line.strip() for line in file if line.strip()]

grid = [list(line) for line in lines]
rows, cols = len(grid), len(grid[0])

# --- Find start position ---
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '^':
            start_row, start_col = i, j
            grid[i][j] = '.'
            break
    else:
        continue
    break


# --- Core movement simulation ---
def walk_path(grid, start_row, start_col):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    r, c, dir_idx = start_row, start_col, 0
    visited = set()
    states = set()
    steps = 0
    max_steps = rows * cols * 4  # absolute safety bound

    while steps < max_steps:
        steps += 1
        visited.add((r, c))
        dr, dc = directions[dir_idx]
        nr, nc = r + dr, c + dc

        # Guard exits the map
        if not (0 <= nr < rows and 0 <= nc < cols):
            return visited, False  # no loop

        # Turn right if obstacle
        if grid[nr][nc] == '#':
            dir_idx = (dir_idx + 1) % 4
            continue

        # Move forward
        r, c = nr, nc
        state = (r, c, dir_idx)
        if state in states:
            return visited, True  # detected loop safely
        states.add(state)

    # Safety cutoff (should never reach here)
    return visited, True


# --- Part 1 ---
visited, _ = walk_path(grid, start_row, start_col)
print(f"Part 1 distinct positions: {len(visited)}")

# --- Part 2 ---
# We only test positions actually visited, others can't change path behavior
candidates = [pos for pos in visited if pos != (start_row, start_col)]

loop_positions = 0

for fr, fc in candidates:
    grid[fr][fc] = '#'  # temporarily place obstacle
    _, is_loop = walk_path(grid, start_row, start_col)
    if is_loop:
        loop_positions += 1
    grid[fr][fc] = '.'  # revert

print(f"Part 2 loop positions: {loop_positions}")
