def mudarOrientacao(robo, comando, bussula):
    if comando == "D":
        try:
            robo = bussula[bussula.index(robo) + 1]
            return robo
        except IndexError:
            return bussula[0]
    else:
        try:
            robo = bussula[bussula.index(robo) - 1]
            return robo
        except IndexError:
            return bussula[2]


while True:
    n, m, s = map(int, input().split())
    if n == 0 and m == 0 and s == 0:
        break
    matriz = []
    bussula = ["N", "L", "S", "O"]
    for i in range(n):
        linha = list(input())
        matriz.append(linha)
        for j in range(m):
            if linha[j] in bussula:
                x = i
                y = j
                robo = matriz[i][j]
    comando = input()
    count = 0
    for c in comando:
        if c == "D" or c == "E":
            robo = mudarOrientacao(robo, c, bussula)
            matriz[x][y] = robo
        else:
            try:
                if robo == "N":
                    if x - 1 == -1 or matriz[x - 1][y] == "#":
                        pass
                    else:
                        if matriz[x - 1][y] == "*":
                            count += 1
                        matriz[x - 1][y] = robo
                        matriz[x][y] = "."
                        x -= 1
                elif robo == "O":
                    if y - 1 == -1 or matriz[x][y - 1] == "#":
                        pass
                    else:
                        if matriz[x][y - 1] == "*":
                            count += 1
                        matriz[x][y - 1] = robo
                        matriz[x][y] = "."
                        y -= 1
                elif robo == "S":
                    if matriz[x + 1][y] == "#":
                        pass
                    else:
                        if matriz[x + 1][y] == "*":
                            count += 1
                        matriz[x + 1][y] = robo
                        matriz[x][y] = "."
                        x += 1
                else:
                    if matriz[x][y + 1] == "#":
                        pass
                    else:
                        if matriz[x][y + 1] == "*":
                            count += 1
                        matriz[x][y + 1] = robo
                        matriz[x][y] = "."
                        y += 1
            except IndexError:
                pass
    print(count)

















