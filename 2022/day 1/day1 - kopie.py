A = ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']
B = []
i = 0

while i < len(A):
    group = []
    while i < len(A) and A[i] != '':
        group.append(A[i])
        i += 1
    if group:
        B.append(group)
    i += 1  
print(B)
###
A = ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']
B = []
i = 0

while i < len(A):
    group_sum = 0
    while i < len(A) and A[i] != '':
        group_sum += int(A[i])
        i += 1
    if group_sum:
        B.append(group_sum)
    i += 1  # skip the empty string

print(B)
C = max(B)
print(C)
###
