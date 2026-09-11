#Satelite


matriz = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]
matriz1 = [
    ["","","",""],
    ["","","",""],
    ["","","",""],
    ["","","",""],
]

for i in range(4):
    for j in range(4):
        matriz1[j][3-i] = matriz[i][j]

for i in range(4):
    print(matriz[i][0], matriz[i][1], matriz[i][2],matriz[i][3])
print()
for i in range(4):
    print(matriz1[i][0], matriz1[i][1], matriz1[i][2],matriz1[i][3])