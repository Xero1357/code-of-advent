from functools import lru_cache

# --- Load input file ---
with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day19.txt") as f:
    sections = f.read().strip().split("\n\n")

patterns = sections[0].split(", ")
designs = sections[1].splitlines()

# --- Part 1: How many designs are possible ---
def can_make(design):
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(n):
        if not dp[i]:
            continue
        for p in patterns:
            if design.startswith(p, i):
                dp[i + len(p)] = True

    return dp[n]

part1 = sum(can_make(d) for d in designs)
print(part1)  # Only the answer, no extra text

# --- Part 2: Total number of different ways to make all designs ---
@lru_cache(None)
def count_ways(design):
    if not design:
        return 1
    total = 0
    for p in patterns:
        if design.startswith(p):
            total += count_ways(design[len(p):])
    return total

part2 = sum(count_ways(d) for d in designs)
print(part2)  # Only the answer, no extra text
