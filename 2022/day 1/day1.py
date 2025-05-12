with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\adventofcode challenge\\2022\\day 1\\data.txt", "r") as file:
    map = file.read()
    A = map.split('\n') 
print(map)    
print(A)

#A = ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000'] # example
B = []
i = 0

while i < len(A):
    group_sum = 0
    while i < len(A) and A[i] != '':
        group_sum += int(A[i])
        i += 1
    if group_sum:
        B.append(group_sum)
    i += 1  

print(B)
C = max(B)
print(C)

D = sorted(B, reverse=True)
print(D)
E = sum(D[:3])
print(E)