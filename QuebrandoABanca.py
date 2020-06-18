while True:
    try:
        a, b = map(int, input().split())
        seq = list(input())
        lista = []
        i = 0
        tamanho_lista = a - b
        maior = 0
        j = 0
        while len(lista) < tamanho_lista:
            try:
                while i <= b:
                    if maior < int(seq[i]):
                        maior = int(seq[i])
                    i+=1
                if maior == 0:
                    lista.append(str(max(seq)))
                else:
                    lista.append(str(maior))
                    b -= seq.index(str(maior))
                    seq = seq[seq.index(str(maior)) + 1:]
                    i = 0
                    maior = 0
            except IndexError:
                lista.append(str(seq[j]))
                j+=1
        print("".join(lista))
    except EOFError:
        break
