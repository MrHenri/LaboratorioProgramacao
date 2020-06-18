class No:
    def __init__(self, dado):
        self.prox = None
        self.ant = None
        self.dado = dado

    def __str__(self):
        return str(self.dado)

class ListaCircular:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir(self, dado):
        no = No(dado)
        if self.inicio == None:
            self.inicio = no
            self.fim = no
        else:
            y = self.inicio
            while y is not self.fim:
                y = y.prox
            y.prox = no
            no.ant = y
            no.prox = self.inicio
            self.fim = no

    def somatorio(self):
        y = self.inicio
        soma = 0
        if y.dado < 0:
            return soma
        soma += y.dado
        top = soma
        while y is not self.fim:
            ant = y
            y = y.prox
            soma += y.dado
            top = maior(top, soma)
        return top

def maior(a, b):
    if a > b:
        return a
    else:
        return b

n = int(input())
fatias = list(map(int, input().split()))
l = ListaCircular()
for i in fatias:
    l.inserir(i)

result = 0
for i in range(n):
    soma = l.somatorio()
    result = maior(soma, result)
    l.inicio = l.inicio.prox
    l.fim = l.fim.prox
print(result)




