isla = [
    [5,2,8],
    [1,"X",4],
    [3,9,6]
    ]

print(isla)

for i in range(3):
    print(isla[i][0], isla[i][1], isla[i][2])
#   print(isla[i])

# monedas
monedas=0
columna = -1
fila = -1
for i in range(3):
    for j in range(3):
        if isla[i][j] != "X":
            monedas = monedas + isla[i][j]
        else: 
            fila = i
            columna = j
print(monedas)
print(f"fila {fila}, columna {columna}")