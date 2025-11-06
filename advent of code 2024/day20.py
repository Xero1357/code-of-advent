from collections import deque, defaultdict

# --- Load input file ---
with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day20.txt") as f:
    grid = [list(line.strip()) for line in f if line.strip()]

H, W = len(grid), len(grid[0])
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

# --- Find start and end ---
for y in range(H):
    for x in range(W):
        if grid[y][x] == 'S':
            start = (x, y)
        elif grid[y][x] == 'E':
            end = (x, y)

# --- BFS to compute distances ---
def bfs_from(source):
    q = deque([(source, 0)])
    dist = {source: 0}
    while q:
        (x, y), d = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] != '#' and (nx, ny) not in dist:
                dist[(nx, ny)] = d + 1
                q.append(((nx, ny), d + 1))
    return dist

dist_from_start = bfs_from(start)
dist_to_end = bfs_from(end)
normal_time = dist_from_start[end]

# --- Part 1: same as before (cheat range 2) ---
cheats1 = defaultdict(int)
for (x1, y1), d1 in dist_from_start.items():
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            cheat_len = abs(dx) + abs(dy)
            if cheat_len == 0 or cheat_len > 2:
                continue
            x2, y2 = x1 + dx, y1 + dy
            if (x2, y2) in dist_to_end:
                d2 = dist_to_end[(x2, y2)]
                total = d1 + cheat_len + d2
                saved = normal_time - total
                if saved > 0:
                    cheats1[saved] += 1

part1 = sum(v for k, v in cheats1.items() if k >= 100)
print(part1)  # Only the answer, no extra text

# --- Part 2: optimized (cheat range up to 20) ---
positions = list(dist_from_start.keys())
cheats2 = defaultdict(int)

for (x1, y1), d1 in dist_from_start.items():
    for dy in range(-20, 21):
        y2 = y1 + dy
        if not (0 <= y2 < H):
            continue
        # Instead of all dx, use limited horizontal slice
        for dx in range(-20 + abs(dy), 21 - abs(dy)):
            x2 = x1 + dx
            if not (0 <= x2 < W):
                continue
            cheat_len = abs(dx) + abs(dy)
            if cheat_len == 0 or cheat_len > 20:
                continue
            if (x2, y2) in dist_to_end:
                d2 = dist_to_end[(x2, y2)]
                total = d1 + cheat_len + d2
                saved = normal_time - total
                if saved > 0:
                    cheats2[saved] += 1

part2 = sum(v for k, v in cheats2.items() if k >= 100)
print(part2)  # Only the answer, no extra text
