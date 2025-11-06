from collections import defaultdict

# --- Load input file ---
with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day23.txt") as f:
    connections = [line.strip() for line in f if line.strip()]

# --- Build undirected graph ---
graph = defaultdict(set)
for line in connections:
    a, b = line.split("-")
    graph[a].add(b)
    graph[b].add(a)

# --- Part 1: Count triangles containing at least one 't' ---
triangles = set()

nodes = sorted(graph.keys())
for i, a in enumerate(nodes):
    for b in graph[a]:
        if b <= a:
            continue
        common = graph[a].intersection(graph[b])
        for c in common:
            if c <= b:
                continue
            triangles.add(tuple(sorted([a, b, c])))

count_part1 = sum(1 for tri in triangles if any(name.startswith("t") for name in tri))
print(count_part1)

# --- Part 2: Find largest fully connected group (maximum clique) ---
# We'll use a Bron–Kerbosch recursive algorithm without pivot for clarity

def bron_kerbosch(R, P, X):
    if not P and not X:
        yield R
        return
    for v in list(P):
        yield from bron_kerbosch(R | {v}, P & graph[v], X & graph[v])
        P.remove(v)
        X.add(v)

# Run the clique finder
all_nodes = set(graph.keys())
max_clique = set()

for clique in bron_kerbosch(set(), all_nodes, set()):
    if len(clique) > len(max_clique):
        max_clique = clique

# Format the password: sorted alphabetically, joined by commas
password = ",".join(sorted(max_clique))
print(password)
