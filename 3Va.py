def verificar(a, b, c):
    matriz[a][b] = 0
    for i in range(c):
        if matriz[b][i] == 1:
            verificar(b, i, n)
    return 1


n, m = map(int, input().split())
matriz = []
for i in range(n):
    matriz+= [[0]*n]
for i in range(m):
    a, b = map(int, input().split())
    a-=1
    b-=1
    matriz[a][b] = 1
total = 0
for i in range(n):
    for j in range(n):
        if matriz[i][j] == 1:
            total += verificar(i, j, n)
print(total)
