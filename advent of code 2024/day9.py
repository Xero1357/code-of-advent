with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day9.txt", "r") as file:
    data = file.read().strip()

disk = []
file_id = 0
for i, c in enumerate(data):
    n = int(c)
    if i % 2 == 0:
        disk.extend([file_id] * n)
        file_id += 1
    else:
        disk.extend(['.'] * n)

l, r = 0, len(disk) - 1
while l < r:
    if disk[l] != '.':
        l += 1
        continue
    if disk[r] == '.':
        r -= 1
        continue
    disk[l], disk[r] = disk[r], '.'
    l += 1
    r -= 1

checksum1 = sum(i * v for i, v in enumerate(disk) if v != '.')
print("Part 1:", checksum1)

disk = []
file_id = 0
for i, c in enumerate(data):
    n = int(c)
    if i % 2 == 0:
        disk.extend([file_id] * n)
        file_id += 1
    else:
        disk.extend(['.'] * n)

files = {}
spaces = []
i = 0
while i < len(disk):
    if disk[i] == '.':
        j = i
        while j < len(disk) and disk[j] == '.':
            j += 1
        spaces.append((i, j - i))
        i = j
    else:
        fid = disk[i]
        j = i
        while j < len(disk) and disk[j] == fid:
            j += 1
        files[fid] = (i, j - i)
        i = j

for fid in sorted(files.keys(), reverse=True):
    pos, size = files[fid]
    for si, (spos, ssize) in enumerate(spaces):
        if ssize >= size and spos < pos:
            for k in range(size):
                disk[spos + k] = fid
                disk[pos + k] = '.'
            new_spaces = []
            if ssize > size:
                new_spaces.append((spos + size, ssize - size))
            for s2 in spaces[:si]:
                new_spaces.append(s2)
            for s2 in spaces[si + 1:]:
                if s2[0] > pos:
                    break
                new_spaces.append(s2)
            spaces = sorted(new_spaces + [(pos, size)], key=lambda x: x[0])
            break

checksum2 = sum(i * v for i, v in enumerate(disk) if v != '.')
print("Part 2:", checksum2)
