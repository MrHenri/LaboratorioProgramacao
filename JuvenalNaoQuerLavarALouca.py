class No:
    def __init__(self, dado):
        self._dado = dado
        self._prox = None
        self._ant = None
    def setDado(self, dado):
        self._dado = dado
    def getDado(self):
        return self._dado
    def setProx(self, prox):
        self._prox = prox
    def getProx(self):
        return self._prox
    def setAnt(self, ant):
        self._ant = ant
    def getAnt(self):
        return self._ant
    def __str__(self):
        return self.getDado()


class CartasDeJogadores:
    def __init__(self):
        self._inicio = None
        self._fim = None
    def setInicio(self, inicio):
        self._inicio = inicio
    def getInicio(self):
        return self._inicio
    def setFim(self, fim):
        self._fim = fim
    def getFim(self):
        return self._fim

    def inserir(self, dado):
        no = No(dado)
        if self._fim == None:
            self._inicio = no
            self._fim = no
            no.setProx(no)
            no.setAnt(no)
        else:
            self._fim.setProx(no)
            no.setAnt(self._fim)
            self._fim = no
            self._fim.setProx(self._inicio)
            self._inicio.setAnt(self._fim)

    def remove(self, no):
        no.getAnt().setProx(no.getProx())
        no.getProx().setAnt(no.getAnt())

c = CartasDeJogadores()
jogos = int(input())
j = 0
listaDeVitoria = ""
while j < jogos:
    try:
        listaDeJogadores = []
        cartasDaMesa = list(input().split())
        while True:
            cartas = input()
            if cartas == "-1":
                j += 1
                break
            for i in cartas.split():
                c.inserir(i)
            listaDeJogadores.append(c.getInicio())
            c.setInicio(None)
            c.setFim(None)
    except EOFError:
        break
    i = 0
    cond = False
    for k in range(1000):
        if i >= len(cartasDaMesa):
            i = 0
        for g in range(len(listaDeJogadores)):
            if listaDeJogadores[g].getDado() == cartasDaMesa[i]:
                if listaDeJogadores[g] == listaDeJogadores[g].getProx():
                    cond = True
                    break
                listaDeJogadores[g] = listaDeJogadores[g].getProx()
                c.remove(listaDeJogadores[g].getAnt())
            else:
                listaDeJogadores[g] = listaDeJogadores[g].getProx()
        if cond == True:
            break
        i += 1
    if cond == False:
        listaDeVitoria += "0 "
    else:
        listaDeVitoria += str(g+1) + " "
for i in listaDeVitoria.split():
    print(i)
