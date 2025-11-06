from functools import lru_cache

with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day10.txt", "r") as file:
    data = file.read().strip().split('\n')

grid = [[int(c) for c in line] for line in data]
h, w = len(grid), len(grid[0])
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs_score(sx, sy):
    from collections import deque
    q = deque([(sx, sy)])
    visited = set([(sx, sy)])
    nines = set()
    while q:
        x, y = q.popleft()
        if grid[y][x] == 9:
            nines.add((x, y))
            continue
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                if grid[ny][nx] == grid[y][x] + 1:
                    visited.add((nx, ny))
                    q.append((nx, ny))
    return len(nines)

@lru_cache(None)
def dfs_count(x, y):
    if grid[y][x] == 9:
        return 1
    total = 0
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] == grid[y][x] + 1:
            total += dfs_count(nx, ny)
    return total

part1 = 0
part2 = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == 0:
            part1 += bfs_score(x, y)
            part2 += dfs_count(x, y)

print("Part 1:", part1)
print("Part 2:", part2)
