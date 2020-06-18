l,c,m,n = map(int, input().split())
matriz = []
for i in range(l+1):
    matriz+= [[0]*(c+1)]
for i in range(1,l+1):
    linha = input().split()
    for j in range(1,c+1):
        matriz[i][j] = int(linha[j-1])
matrizAux = []
for i in range(l+1):
    matrizAux+=[[0]*(c+1)]
for i in range(1, l+1):
    for j in range(1, c+1):
        matrizAux[i][j] = matrizAux[i-1][j] + matrizAux[i][j-1] - matrizAux[i-1][j-1] + matriz[i][j]
result = 0
for i in range(m, l+1):
    for j in range(n, c+1):
        total = matrizAux[i][j] - matrizAux[i-m][j] - matrizAux[i][j-n] + matrizAux[i-m][j-n]
        if total > result:
            result = total
print(result)
