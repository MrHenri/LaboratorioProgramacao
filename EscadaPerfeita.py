def soma(lista):
    total = 0
    for i in range(len(lista)):
        total+= lista[i]
    return total

n = int(input())
escada = list(map(int, input().split()))
total = soma(escada) - int((n*(n+1))/2)
if total >= 0 and total % n == 0:
    movimentos = 0
    tamanho = int(total/n) + 1
    for i in range(n):
        if escada[i] > tamanho:
            movimentos += escada[i] - tamanho
        tamanho+=1
    print(movimentos)
else:
    print(-1)




