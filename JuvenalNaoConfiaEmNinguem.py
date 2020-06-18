def navio(linha, coluna, mapa, n, m, c, tamanho):
  mapa[linha][coluna] = c
  if linha < n - 1 and mapa[linha+1][coluna] == "#":
    tamanho = navio(linha + 1, coluna, mapa, n, m, c, tamanho+1)
  if linha > 0 and mapa[linha-1][coluna] == "#":
    tamanho = navio(linha - 1, coluna, mapa, n, m, c, tamanho+1)
  if coluna < m - 1 and mapa[linha][coluna+1] == "#":
    tamanho = navio(linha, coluna + 1, mapa, n, m, c, tamanho+1)
  if coluna > 0 and mapa[linha][coluna-1] == "#":
    tamanho = navio(linha, coluna - 1, mapa, n, m, c, tamanho+1)
  return tamanho

n, m = map(int, input().split())
matriz = []
for i in range(n):
  matriz+= [[0]*m]
for i in range(n):
  linha = input()
  for j in range(m):
    matriz[i][j] = linha[j]
navios = []
count = 0
for i in range(n):
  for j in range(m):
    if matriz[i][j] == "#":
      navios.append(navio(i,j,matriz,n,m,count, 1))
      count+=1
k = int(input())
for i in range(k):
  l, c = map(int, input().split())
  l-=1
  c-=1
  if matriz[l][c] != ".":
    navios[matriz[l][c]] -= 1
count = 0
for i in range((len(navios))):
  if navios[i] == 0:
    count+=1
print(count)







