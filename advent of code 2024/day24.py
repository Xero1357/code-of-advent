import sys
from collections import defaultdict, deque

# ------------------------------------------------------------
# 1. Load and parse the puzzle input (fixed path)
# ------------------------------------------------------------
with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day24.txt") as f:
    init, gates = f.read().strip().split("\n\n")

# initial wire values (only x.. and y..)
init_vals = {}
for line in init.splitlines():
    w, v = line.split(": ")
    init_vals[w] = int(v)

# gate list: (a, op, b, out)
gate_list = []
gate_by_out = {}
for line in gates.splitlines():
    left, out = line.split(" -> ")
    a, op, b = left.split()
    gate_list.append((a, op, b, out))
    gate_by_out[out] = (a, op, b)

# ------------------------------------------------------------
# 2. Helper: topological simulation
# ------------------------------------------------------------
def simulate(start_vals):
    vals = dict(start_vals)
    pending = deque(gate_list)
    while pending:
        a, op, b, out = pending.popleft()
        if a not in vals or b not in vals:
            pending.append((a, op, b, out))
            continue
        if op == "AND":
            vals[out] = vals[a] & vals[b]
        elif op == "OR":
            vals[out] = vals[a] | vals[b]
        elif op == "XOR":
            vals[out] = vals[a] ^ vals[b]
    return vals

# ------------------------------------------------------------
# 3. Identify carry wires (internal chain)
# ------------------------------------------------------------
all_wires = set(init_vals) | set(gate_by_out)
x_wires = {w for w in init_vals if w.startswith("x")}
y_wires = {w for w in init_vals if w.startswith("y")}
z_wires = {w for w in gate_by_out if w.startswith("z")}

carry_candidates = all_wires - x_wires - y_wires - z_wires

produced = defaultdict(list)
consumed = defaultdict(list)
for a, op, b, out in gate_list:
    produced[out].append((a, op, b))
    consumed[a].append(out)
    consumed[b].append(out)

carry_wires = []
for w in carry_candidates:
    if len(produced[w]) == 1 and len(consumed[w]) == 1:
        carry_wires.append(w)

carry_wires.sort(key=lambda w: (len(w), w))

# ------------------------------------------------------------
# 4. Find broken carry links using all-zero input
# ------------------------------------------------------------
def check_carry_chain():
    vals = {w: 0 for w in x_wires | y_wires}
    result = simulate(vals)

    broken = []                               # (bit_index, wrong_carry_in_wire)
    for i in range(len(carry_wires) - 1):
        cur = carry_wires[i]
        nxt = carry_wires[i + 1]
        if result.get(nxt, 0) != result.get(cur, 0):
            broken.append((i, nxt))           # nxt should have received cur's value
    return broken

broken_links = check_carry_chain()            # exactly 4 entries

# ------------------------------------------------------------
# 5. Collect the 8 wires that need swapping
# ------------------------------------------------------------
swapped_outputs = set()

for bit_idx, wrong_carry_in in broken_links:
    correct_carry_out = carry_wires[bit_idx]

    # gate that writes the wrong carry-in
    out_wrong = wrong_carry_in
    # gate that writes the correct carry-out
    out_correct = correct_carry_out

    swapped_outputs.add(out_wrong)
    swapped_outputs.add(out_correct)

# ------------------------------------------------------------
# 6. Output the answer
# ------------------------------------------------------------
answer = ",".join(sorted(swapped_outputs))
print("Part 2:", answer)