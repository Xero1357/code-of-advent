# ---------------- Read data ----------------
with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day14.txt", "r") as file:
    data = file.read()

lines = data.split('\n')

# Parse the robot positions and velocities
robots = []
for line in lines:
    if line.strip():
        # Example line: p=0,4 v=3,-3
        p_part, v_part = line.split(' v=')
        x, y = map(int, p_part[2:].split(','))
        vx, vy = map(int, v_part.split(','))
        robots.append((x, y, vx, vy))

# ---------------- Part 1: Safety factor ----------------
width = 101
height = 103
t = 100

# Compute positions after t seconds with wraparound
positions = []
for x, y, vx, vy in robots:
    new_x = (x + vx * t) % width
    new_y = (y + vy * t) % height
    positions.append((new_x, new_y))

# Compute safety factor by quadrants
mid_x = width // 2
mid_y = height // 2
quad_counts = [0, 0, 0, 0]  # top-left, top-right, bottom-left, bottom-right

for x, y in positions:
    if x == mid_x or y == mid_y:
        continue  # Skip robots exactly on the middle lines
    if x < mid_x and y < mid_y:
        quad_counts[0] += 1  # top-left
    elif x >= mid_x and y < mid_y:
        quad_counts[1] += 1  # top-right
    elif x < mid_x and y >= mid_y:
        quad_counts[2] += 1  # bottom-left
    else:
        quad_counts[3] += 1  # bottom-right

safety_factor = quad_counts[0] * quad_counts[1] * quad_counts[2] * quad_counts[3]

print("----- Part 1 -----")
print("Quadrant counts:", quad_counts)
print("Safety factor after 100 seconds:", safety_factor)

# ---------------- Part 2: Easter egg ----------------
# Strategy: Find the time t where the bounding box of all robots is smallest
best_t = None
min_area = float('inf')
best_positions = []

# We'll simulate for a reasonable range of seconds. Adjust if needed.
for t in range(20000):
    positions = [(x + vx * t, y + vy * t) for x, y, vx, vy in robots]
    xs = [pos[0] for pos in positions]
    ys = [pos[1] for pos in positions]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    area = (max_x - min_x + 1) * (max_y - min_y + 1)
    
    if area < min_area:
        min_area = area
        best_t = t
        best_positions = positions

print("\n----- Part 2 -----")
print("Fewest seconds until Easter egg appears:", best_t)
print("Bounding box size:", min_area)

# Visualize the Easter egg
positions_set = set(best_positions)
xs = [pos[0] for pos in best_positions]
ys = [pos[1] for pos in best_positions]
min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)

for y in range(min_y, max_y + 1):
    line = ""
    for x in range(min_x, max_x + 1):
        line += "#" if (x, y) in positions_set else "."
    print(line)
