from collections import deque, defaultdict

with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day12.txt") as f:
    grid = [list(line.strip()) for line in f if line.strip()]

rows, cols = len(grid), len(grid[0])
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs_region(sr, sc, visited):
    plant = grid[sr][sc]
    q = deque([(sr, sc)])
    visited.add((sr, sc))
    region = []
    while q:
        r, c = q.popleft()
        region.append((r, c))
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == plant:
                visited.add((nr,nc))
                q.append((nr,nc))
    return region

def compute_metrics(region):
    region_set = set(region)
    area = len(region)
    horiz, vert = set(), set()

    for r, c in region:
        if not (0 <= r-1 < rows and (r-1, c) in region_set):
            horiz.add((r, c))
        if not (0 <= r+1 < rows and (r+1, c) in region_set):
            horiz.add((r+1, c))
        if not (0 <= c-1 < cols and (r, c-1) in region_set):
            vert.add((c, r))
        if not (0 <= c+1 < cols and (r, c+1) in region_set):
            vert.add((c+1, r))

    perimeter = len(horiz) + len(vert)

    seen = set()
    sides = 0

    def dfs_h(y, x):
        stack = [(y, x)]
        while stack:
            yy, xx = stack.pop()
            if (yy, xx) in seen:
                continue
            seen.add((yy, xx))
            for nx in [xx-1, xx+1]:
                if (yy, nx) in horiz and (yy, nx) not in seen:
                    stack.append((yy, nx))

    def dfs_v(x, y):
        stack = [(x, y)]
        while stack:
            xx, yy = stack.pop()
            if (xx, yy) in seen:
                continue
            seen.add((xx, yy))
            for ny in [yy-1, yy+1]:
                if (xx, ny) in vert and (xx, ny) not in seen:
                    stack.append((xx, ny))

    for h in horiz:
        if h not in seen:
            dfs_h(*h)
            sides += 1
    for v in vert:
        if v not in seen:
            dfs_v(*v)
            sides += 1

    return area, perimeter, sides

visited = set()
total_part1 = 0
total_part2 = 0

for r in range(rows):
    for c in range(cols):
        if (r, c) not in visited:
            region = bfs_region(r, c, visited)
            area, perim, sides = compute_metrics(region)
            total_part1 += area * perim
            total_part2 += area * sides

print("Part 1 total (area * perimeter):", total_part1)
print("Part 2 total (area * sides):", total_part2)
