import re

with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day3.txt", "r") as file:
    data = file.read()
print(data)

mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
muls = [(int(x), int(y)) for x, y in re.findall(mul_pattern, data)]
part1_total = sum(x * y for x, y in muls)

do_dont_pattern = r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))'
instructions = re.findall(do_dont_pattern, data)
enabled = True
part2_muls = []
for inst in instructions:
    if inst[0] == 'do()':
        enabled = True
    elif inst[0] == "don't()":
        enabled = False
    elif enabled:
        x, y = int(inst[1]), int(inst[2])
        part2_muls.append((x, y))
part2_total = sum(x * y for x, y in part2_muls)

print("All mul instructions:", muls)
print("Part 1 total:", part1_total)
print("Instructions:", instructions)
print("Enabled mul instructions:", part2_muls)
print("Part 2 total:", part2_total)