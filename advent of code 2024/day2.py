with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day2.txt", "r") as file:
    data = file.read()
    lines = data.split('\n')
print(data)
print(lines)

numbers = [[int(x) for x in line.split()] for line in lines if line.strip()]

def is_safe(levels):
    if len(levels) < 2:
        return True
    diffs = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    all_inc = all(d > 0 for d in diffs)
    all_dec = all(d < 0 for d in diffs)
    if not (all_inc or all_dec):
        return False
    return all(1 <= abs(d) <= 3 for d in diffs)

part1_safe = sum(1 for nums in numbers if is_safe(nums))

part2_safe = 0
for nums in numbers:
    if is_safe(nums):
        part2_safe += 1
        continue
    for i in range(len(nums)):
        removed = nums[:i] + nums[i+1:]
        if len(removed) >= 2 and is_safe(removed):
            part2_safe += 1
            break

print("Numbers per report:", numbers)
print("Part 1 safe reports:", part1_safe)
print("Part 2 safe reports:", part2_safe)