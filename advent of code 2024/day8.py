with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day8.txt", "r") as file:
    data = file.read().strip().split('\n')

grid = [list(line) for line in data]
h, w = len(grid), len(grid[0])
antennas = {}
for y in range(h):
    for x in range(w):
        c = grid[y][x]
        if c != '.':
            antennas.setdefault(c, []).append((x, y))

antinodes1 = set()
for freq, coords in antennas.items():
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            dx, dy = x2 - x1, y2 - y1
            ax1, ay1 = x1 - dx, y1 - dy
            ax2, ay2 = x2 + dx, y2 + dy
            if 0 <= ax1 < w and 0 <= ay1 < h:
                antinodes1.add((ax1, ay1))
            if 0 <= ax2 < w and 0 <= ay2 < h:
                antinodes1.add((ax2, ay2))

antinodes2 = set()
for freq, coords in antennas.items():
    if len(coords) < 2:
        continue
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i == j:
                continue
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            dx, dy = x2 - x1, y2 - y1
            x, y = x1 - dx, y1 - dy
            while 0 <= x < w and 0 <= y < h:
                antinodes2.add((x, y))
                x -= dx
                y -= dy
            x, y = x1 + dx, y1 + dy
            while 0 <= x < w and 0 <= y < h:
                antinodes2.add((x, y))
                x += dx
                y += dy
    for (x, y) in coords:
        antinodes2.add((x, y))

print("Part 1:", len(antinodes1))
print("Part 2:", len(antinodes2))
