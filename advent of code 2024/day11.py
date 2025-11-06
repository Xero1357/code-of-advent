from functools import lru_cache

with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day11.txt", "r") as file:
    stones = list(map(int, file.read().strip().split()))

@lru_cache(None)
def count_after_blinks(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return count_after_blinks(1, blinks - 1)
    s = str(stone)
    if len(s) % 2 == 0:
        mid = len(s) // 2
        left = int(s[:mid])
        right = int(s[mid:])
        return count_after_blinks(left, blinks - 1) + count_after_blinks(right, blinks - 1)
    return count_after_blinks(stone * 2024, blinks - 1)

part1 = sum(count_after_blinks(stone, 25) for stone in stones)
part2 = sum(count_after_blinks(stone, 75) for stone in stones)

print("Part 1:", part1)
print("Part 2:", part2)
