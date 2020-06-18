import sys
sys.setrecursionlimit(10000)

def buscarPasto(linha, coluna, mapa, n, m, animais):
    if mapa[linha][coluna] == "#" or mapa[linha][coluna] == "Passado":
        return animais
    elif mapa[linha][coluna] == "k":
        animais[0]+=1
    elif mapa[linha][coluna] == "v":
        animais[1]+=1
    mapa[linha][coluna] = "Passado"

    if linha > 0:
        buscarPasto(linha-1, coluna, mapa, n, m, animais)
    if coluna < m+1:
        buscarPasto(linha, coluna + 1, mapa, n, m, animais)
    if linha < n+1:
        buscarPasto(linha + 1, coluna, mapa, n, m, animais)
    if coluna > 0:
        buscarPasto(linha, coluna - 1, mapa, n, m, animais)
    return animais

n, m = map(int,input().split())
matriz = []
for i in range(n):
    matriz+= [[0]*m]
for i in range(n):
    linha = input()
    for j in range(m):
        matriz[i][j] = linha[j]
ovelha = 0
lobo = 0
for i in range(n):
    for j in range(m):
        animais = [0]*2
        if matriz[i][j] == "v" or matriz[i][j] == "k":
            animais = buscarPasto(i, j, matriz, n, m, animais)
            if animais[0] > animais[1]:
                ovelha+= animais[0]
            else:
                lobo+= animais[1]
print(ovelha, lobo)
