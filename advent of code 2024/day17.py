# --- Chronospatial Computer Emulator ---
def run_program(A, program):
    B = 0
    C = 0
    ip = 0
    output = []

    def combo_value(op):
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

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        jump = False

        if opcode == 0:  # adv
            denom = 2 ** combo_value(operand)
            A = A // denom
        elif opcode == 1:  # bxl
            B = B ^ operand
        elif opcode == 2:  # bst
            B = combo_value(operand) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                ip = operand
                jump = True
        elif opcode == 4:  # bxc
            B = B ^ C
        elif opcode == 5:  # out
            output.append(combo_value(operand) % 8)
        elif opcode == 6:  # bdv
            denom = 2 ** combo_value(operand)
            B = A // denom
        elif opcode == 7:  # cdv
            denom = 2 ** combo_value(operand)
            C = A // denom
        else:
            raise ValueError(f"Unknown opcode {opcode}")

        if not jump:
            ip += 2

    return output


# --- Part 1 ---
with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day17.txt") as f:
    lines = f.read().splitlines()

program_line = [line for line in lines if line.startswith("Program:")][0]
program = [int(x) for x in program_line.split(":")[1].strip().split(",")]

# Initial registers for part 1
A = 51064159
output = run_program(A, program)
print("Part 1 Output:", ",".join(map(str, output)))


# --- Part 2 ---
# We want the smallest A such that the program output equals the program itself.
target = program

# Cache to speed up recursion
from functools import lru_cache

@lru_cache(None)
def find_a(index, suffix):
    """
    Returns all possible A values that produce the last (len(target)-index) outputs.
    """
    if index == len(target):
        return {0}  # base case: A = 0 works for empty suffix

    next_values = set()
    for partial_a in find_a(index + 1, tuple(target[index + 1:])):
        for extra_bits in range(8):
            candidate_a = (partial_a << 3) | extra_bits
            out = run_program(candidate_a, program)
            # We only need the last len(target) - index outputs
            if out == target[index:]:
                next_values.add(candidate_a)
    return next_values


# Efficient reverse search (iteratively instead of recursion)
candidates = {0}
for value in reversed(target):
    new_candidates = set()
    for base in candidates:
        for x in range(8):
            candidate = (base << 3) | x
            out = run_program(candidate, program)
            if out == target[-len(out):]:
                new_candidates.add(candidate)
    candidates = new_candidates

print("Part 2 Possible A values:", candidates)
if candidates:
    print("Part 2 Answer (lowest A):", min(candidates))
