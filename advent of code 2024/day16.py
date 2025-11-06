from heapq import heappush, heappop
from collections import defaultdict, deque

# Load the Day 17 program from file
with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day17.txt") as f:
    program = [int(x) for x in f.read().strip().split(",")]

# Initial registers
A_init, B_init, C_init = 51064159, 0, 0
ip_init = 0  # instruction pointer

# Heap for Dijkstra-style processing (steps, state)
heap = [(0, (A_init, B_init, C_init, ip_init))]
best = {}  # state -> minimal steps
prev = defaultdict(list)  # for backtracking
outputs = defaultdict(list)  # state -> list of outputs

# Helper function for combo operands
def get_combo_value(op, A, B, C):
    if 0 <= op <= 3:
        return op
    elif op == 4:
        return A
    elif op == 5:
        return B
    elif op == 6:
        return C
    else:
        raise ValueError("Invalid combo operand")

# Process the program
while heap:
    steps, (A, B, C, ip) = heappop(heap)
    state = (A, B, C, ip)

    if state in best and best[state] <= steps:
        continue
    best[state] = steps

    if ip >= len(program):
        continue  # Program halts

    opcode = program[ip]
    operand = program[ip + 1]
    jump = False

    new_A, new_B, new_C, new_ip = A, B, C, ip + 2

    if opcode == 0:  # adv
        denom = 2 ** get_combo_value(operand, A, B, C)
        new_A = A // denom
    elif opcode == 1:  # bxl
        new_B = B ^ operand
    elif opcode == 2:  # bst
        new_B = get_combo_value(operand, A, B, C) % 8
    elif opcode == 3:  # jnz
        if A != 0:
            new_ip = operand
            jump = True
    elif opcode == 4:  # bxc
        new_B = B ^ C
    elif opcode == 5:  # out
        val = get_combo_value(operand, A, B, C) % 8
        outputs[state].append(val)
    elif opcode == 6:  # bdv
        denom = 2 ** get_combo_value(operand, A, B, C)
        new_B = A // denom
    elif opcode == 7:  # cdv
        denom = 2 ** get_combo_value(operand, A, B, C)
        new_C = A // denom
    else:
        raise ValueError(f"Unknown opcode {opcode}")

    # Record previous state for potential backtracking
    prev[(new_A, new_B, new_C, new_ip)].append(state)
    heappush(heap, (steps + 1, (new_A, new_B, new_C, new_ip)))

# Reconstruct program output in instruction order
final_output = []
for state in sorted(outputs, key=lambda s: s[3]):
    final_output.extend(outputs[state])

print("Program output:", ",".join(map(str, final_output)))
