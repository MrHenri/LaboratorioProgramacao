def minimo(a,b,c):
    if a < b and a < c:
        mini = a
    elif b < a and b < c:
        mini = b
    else:
        mini = c
    return mini

def distanciaDeEdicao(analisada, dicionario):
    for j in range(1, len(dicionario)):
        matriz[0][j] = j
    for i in range(1, len(analisada)):
        matriz[i][0] = i
        for j in range(1, len(dicionario)):
            if dicionario[j] == analisada[i]:
                matriz[i][j] = matriz[i-1][j-1]
            else:
                matriz[i][j] = minimo(matriz[i-1][j], matriz[i][j-1], matriz[i-1][j-1]) + 1
    return matriz[i][j]

n, m = map(int, input().split())
palavrasDicionario = [""]*n
palavrasAnalisadas = [""]*m
for i in range(n):
    palavrasDicionario[i] = " " + input()

for i in range(m):
    palavrasAnalisadas[i] = " " + input()


for i in range(len(palavrasAnalisadas)):
    results = ""
    for j in range(len(palavrasDicionario)):
        matriz = []
        tamanhoPalavrasDicionario = len(palavrasDicionario[j])
        tamanhoPalavrasAnalisadas = len(palavrasAnalisadas[i])
        for k in range(tamanhoPalavrasAnalisadas):
            matriz += [[0]*(tamanhoPalavrasDicionario)]
        nEdicao = distanciaDeEdicao(palavrasAnalisadas[i], palavrasDicionario[j])
        if nEdicao <= 2:
            results += palavrasDicionario[j]
    print(results.strip(" "))

