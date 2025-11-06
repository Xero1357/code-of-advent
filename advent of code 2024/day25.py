with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day25.txt", "r") as file:
    data = file.read().strip()

schematics = [s.split('\n') for s in data.split('\n\n')]

locks  = [s for s in schematics if s[0] == '#####']
keys   = [s for s in schematics if s[0] == '.....']

def schematic_to_heights(schematic, is_lock=True):
    rows = len(schematic)
    cols = len(schematic[0])
    heights = []
    for c in range(cols):
        h = 0
        if is_lock:
            for r in range(rows):
                if schematic[r][c] == '#':
                    h += 1
                else:
                    break
        else:
            for r in range(rows-1, -1, -1):
                if schematic[r][c] == '#':
                    h += 1
                else:
                    break
        heights.append(h)
    return heights

lock_heights = [schematic_to_heights(lock, True) for lock in locks]
key_heights  = [schematic_to_heights(key, False) for key in keys]

fit_count = 0
for i, lock in enumerate(lock_heights):
    max_height = len(locks[i])
    for key in key_heights:
        if all(l + k <= max_height for l, k in zip(lock, key)):
            fit_count += 1

print(fit_count)
