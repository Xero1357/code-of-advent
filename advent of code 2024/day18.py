from collections import deque

# --- Load input file ---
with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day18.txt") as f:
    coords = [tuple(map(int, line.split(','))) for line in f if line.strip()]

# --- Configuration ---
GRID_SIZE = 70
LIMIT = 1024
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

# --- BFS shortest path ---
def bfs(blocked):
    start, goal = (0,0), (GRID_SIZE, GRID_SIZE)
    queue = deque([(start,0)])
    seen = {start}
    while queue:
        (x,y), steps = queue.popleft()
        if (x,y) == goal:
            return steps
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if 0 <= nx <= GRID_SIZE and 0 <= ny <= GRID_SIZE:
                if (nx,ny) not in blocked and (nx,ny) not in seen:
                    seen.add((nx,ny))
                    queue.append(((nx,ny), steps+1))
    return None

# --- Part 1 ---
blocked = set(coords[:LIMIT])
steps = bfs(blocked)
print(steps)  # Only the answer, no extra text

# --- Part 2 ---
blocked = set()
for coord in coords:
    blocked.add(coord)
    if bfs(blocked) is None:
        print(f"{coord[0]},{coord[1]}")  # Only coordinates, as requested
        break
