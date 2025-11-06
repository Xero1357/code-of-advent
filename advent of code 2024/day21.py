from collections import deque
from functools import lru_cache

# --- Load input file ---
with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day21.txt") as f:
    codes = [line.strip() for line in f if line.strip()]

# --- Keypad layouts ---
num_pad = {
    "7": (0,0), "8": (0,1), "9": (0,2),
    "4": (1,0), "5": (1,1), "6": (1,2),
    "1": (2,0), "2": (2,1), "3": (2,2),
    "0": (3,1), "A": (3,2)
}
num_invalid = {(3,0)}

dir_pad = {
    "^": (0,1), "A": (0,2),
    "<": (1,0), "v": (1,1), ">": (1,2)
}
dir_invalid = {(0,0)}

dirs = {"^": (-1,0), "v": (1,0), "<": (0,-1), ">": (0,1)}

# --- Precompute shortest paths ---
def bfs_paths(keypad, invalid):
    paths = {}
    for start_key, start_pos in keypad.items():
        dist = {start_pos: ""}
        q = deque([start_pos])
        while q:
            r, c = q.popleft()
            for d, (dr, dc) in dirs.items():
                nr, nc = r + dr, c + dc
                if (nr, nc) in invalid or (nr, nc) not in keypad.values():
                    continue
                if (nr, nc) not in dist:
                    dist[(nr, nc)] = dist[(r, c)] + d
                    q.append((nr, nc))
        for end_key, end_pos in keypad.items():
            if start_key == end_key:
                paths[(start_key, end_key)] = "A"
            else:
                paths[(start_key, end_key)] = dist[end_pos] + "A"
    return paths

num_paths = bfs_paths(num_pad, num_invalid)
dir_paths = bfs_paths(dir_pad, dir_invalid)

# --- Recursive typing length ---
@lru_cache(maxsize=None)
def length_to_type(seq, depth):
    if depth == 0:
        return len(seq)
    total, cur = 0, "A"
    for c in seq:
        total += length_to_type(dir_paths[(cur, c)], depth - 1)
        cur = c
    return total

# --- Convert numeric code to movement sequence ---
def numeric_sequence(code):
    cur, seq = "A", ""
    for ch in code:
        seq += num_paths[(cur, ch)]
        cur = ch
    return seq

# --- Compute total complexity ---
total = 0
for code in codes:
    seq = numeric_sequence(code)
    presses = length_to_type(seq, 2)
    total += presses * int(code[:-1])

print(total)  # Only the final answer
