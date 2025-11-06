with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day13.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip()]

machines = []
i = 0
while i < len(lines):
    # Parse Button A
    a_line = lines[i].split()
    XA = int(a_line[2][2:-1])
    YA = int(a_line[3][2:])
    
    # Parse Button B
    b_line = lines[i+1].split()
    XB = int(b_line[2][2:-1])
    YB = int(b_line[3][2:])
    
    # Parse Prize
    p_coords = lines[i+2].split(':')[1].split(',')
    XP = int(p_coords[0].strip()[2:])
    YP = int(p_coords[1].strip()[2:])
    
    machines.append({"A": (XA, YA), "B": (XB, YB), "Prize": (XP, YP)})
    i += 3

max_presses = 100
token_costs = {"A": 3, "B": 1}

# Part 1 computation
total_tokens_part1 = 0

for machine in machines:
    XA, YA = machine["A"]
    XB, YB = machine["B"]
    XP, YP = machine["Prize"]
    
    min_cost = None
    
    # Try all possible presses of A and B within 0..100
    for a in range(max_presses + 1):
        for b in range(max_presses + 1):
            if a * XA + b * XB == XP and a * YA + b * YB == YP:
                cost = a * token_costs["A"] + b * token_costs["B"]
                if min_cost is None or cost < min_cost:
                    min_cost = cost
    
    if min_cost is not None:
        total_tokens_part1 += min_cost

print("Part 1 - Fewest tokens needed to win all possible prizes:", total_tokens_part1)

# ------------------- Part 2 -------------------
OFFSET = 10_000_000_000_000
total_tokens_part2 = 0

for machine in machines:
    XA, YA = machine["A"]
    XB, YB = machine["B"]
    XP, YP = machine["Prize"]
    
    # Add offset to prize coordinates
    XP2 = XP + OFFSET
    YP2 = YP + OFFSET
    
    # Solve 2x2 system using exact formula
    det = XA*YB - XB*YA
    if det == 0:
        continue  # no solution
    
    a_num = XP2*YB - XB*YP2
    b_num = XA*YP2 - YA*XP2
    
    if a_num % det != 0 or b_num % det != 0:
        continue  # solution not integer
    
    a = a_num // det
    b = b_num // det
    
    if a < 0 or b < 0:
        continue  # only non-negative solutions
    
    total_tokens_part2 += a*token_costs["A"] + b*token_costs["B"]

print("Part 2 - Fewest tokens needed to win all possible prizes:", total_tokens_part2)