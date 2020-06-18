class no:
    def __init__(self,dado):
        self.dado = dado
        self.prox = None
        self.ant = None

    def getDado(self):
        return self.dado

    def setDado(self,dado):
        self.dado = dado

    def getProx(self):
        return self.prox

    def setProx(self,prox):
        self.prox = prox

    def getAnt(self):
        return self.ant

    def setAnt(self,ant):
        self.ant = ant


class listaSimples:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def getInicio(self):
        return self.inicio

    def setInicio(self,inicio):
        self.inicio = inicio

    def getFim(self):
        return self.fim

    def setFim(self,fim):
        self.fim = fim

    def InserirFim(self,dado):
        laco = no(dado)
        if self.inicio == None:
            self.inicio = laco
            self.fim = laco
        else:
            self.fim.setProx(laco)
            self.fim = laco

    def __str__(self):
        x = ""
        y = self.inicio
        while y != None:
            x += y.getDado() + " "
            y = y.getProx()
        return x

class nodo:
    def __init__(self,chave = None,dado = None):
        self.chave = chave
        self.dado = dado
        self.pai = None
        self.filhoEsquerdo = None
        self.filhoDireiro = None

    def setChave(self, chave):
        self.chave = chave
    def getChave(self):
        return self.chave

    def setDado(self, dado):
        self.dado = dado
    def getDado(self):
        return self.dado

    def setPai(self,pai):
        self.pai = pai
    def getPai(self):
        return self.pai

    def setFilhoEsquerdo(self,filhoEsquerdo):
        self.filhoEsquerdo = filhoEsquerdo
    def getFilhoEsquerdo(self):
        return self.filhoEsquerdo

    def setFilhoDireito(self,filhoDireito):
        self.filhoDireiro = filhoDireito
    def getFilhoDireito(self):
        return self.filhoDireiro

    def __str__(self):
        return str(str(self.getChave()))

class Tree:
    def __init__(self):
        self.root = None

    def setRoot(self,root):
        self.root = root
    def getRoot(self):
        return self.root

    def Inserir(self, chave, dado = None):
        chave = nodo(chave,dado)
        y = None
        x = self.root
        while x != None:
            y = x
            if chave.getChave() <= x.getChave():
                x = x.getFilhoEsquerdo()
            else:
                x = x.getFilhoDireito()
        chave.setPai(y)
        if y == None:
            self.root = chave
        elif chave.getChave() <= y.getChave():
            y.setFilhoEsquerdo(chave)
        else:
            y.setFilhoDireito(chave)

    def Buscar(self,chave):
        x = self.root
        if x == None:
            return 0
        if x.getChave() == chave.getChave():
            return x
        while x.getChave() != chave.getChave():
            if chave.getChave() <= x.getChave():
                x = x.getFilhoEsquerdo()
            else:
                x = x.getFilhoDireito()
            if x == None:
                return 0
            if x.getChave() == chave.getChave():
                return x

    def BuscarMaior(self,tree = None):
        if tree == None:
            tree = self.root
        while tree.getFilhoDireito() != None:
            tree = tree.getFilhoDireito()
        return tree
    def BuscarMenor(self,tree = None):
        if tree == None:
            tree = self.root
        while tree.getFilhoEsquerdo() != None:
            tree = tree.getFilhoEsquerdo()
        return tree

    def Sucessor(self,valor):
       valor = self.Buscar(valor)
       if valor.getFilhoDireito() != None:
           return self.BuscarMenor(valor.getFilhoDireito())
       pai = valor.getPai()
       while pai != None and valor == pai.getFilhoDireito():
           valor = pai
           pai = valor.getPai()
       return pai

    def Antecessor(self,valor):
        valor = nodo(valor)
        valor = self.Buscar(valor)
        if valor == 0:
            return 0
        if valor.getFilhoEsquerdo() != None:
            if valor.getFilhoEsquerdo().getChave() == valor.getChave():
                return valor.getPai()
        if valor.getFilhoEsquerdo() != None:
            return self.BuscarMaior(valor.getFilhoEsquerdo())
        pai = valor.getPai()
        while pai != None and valor == pai.getFilhoEsquerdo():
            valor = pai
            pai = valor.getPai()
        return pai

    def EmOrdem(self, tree, lista):
        if tree != None:
            self.EmOrdem(tree.getFilhoEsquerdo(), lista)
            lista.InserirFim(str(tree.getChave()))
            self.EmOrdem(tree.getFilhoDireito(), lista)
        return 0
    def PreOrdem(self, tree, lista):
        if tree != None:
            lista.InserirFim(str(tree.getChave()))
            self.PreOrdem(tree.getFilhoEsquerdo(), lista)
            self.PreOrdem(tree.getFilhoDireito(), lista)
        return 0
    def PosOrdem(self, tree, lista):
        if tree != None:
            self.PosOrdem(tree.getFilhoEsquerdo(), lista)
            self.PosOrdem(tree.getFilhoDireito(), lista)
            lista.InserirFim(str(tree.getChave()))
        return 0

    def Transplante(self,chave,filho):
        if chave.getPai() == None:
            self.root = filho
        elif chave == chave.getPai().getFilhoEsquerdo():
            chave.getPai().setFilhoEsquerdo(filho)
            chave.getPai().setPai(chave)
        else:
            chave.getPai().setFilhoDireito(filho)
            chave.getPai().setPai(chave)
        if filho != None:
            filho.setPai(chave.getPai())
    def Delete(self,chave):
        chave = nodo(chave)
        chave = self.Buscar(chave)
        if chave.getFilhoEsquerdo() == None:
            self.Transplante(chave, chave.getFilhoDireito())
        elif chave.getFilhoDireito() == None:
            self.Transplante(chave, chave.getFilhoEsquerdo())
        else:
            y = self.Sucessor(chave)
            if y.getPai() != chave:
                self.Transplante(y,y.getFilhoEsquerdo())
                y.setFilhoDireito(chave.getFilhoDireito())
                y.setPai(chave)
            self.Transplante(chave,y)
            y.setFilhoEsquerdo(chave.getFilhoEsquerdo())
            y.getFilhoEsquerdo().setPai(y)

caso = 1
while True:
    t = Tree()
    r = []
    n = int(input())
    for i in range(n):
        comando = input().split()
        if comando[0] == "A":
            t.Inserir(int(comando[1]),"A")
        elif comando[0] == "B":
            t.Delete(int(comando[1]))
        elif comando[0] == "C":
            r.append(str(t.Antecessor(int(comando[1]))))
        elif comando[0] == "PRE":
            l = listaSimples()
            t.PreOrdem(t.root,l)
            if l.fim == None:
                r.append("0")
            else:
                r.append(str(l))
        elif comando[0] == "IN":
            l = listaSimples()
            t.EmOrdem(t.root,l)
            if l.fim == None:
                r.append("0")
            else:
                r.append(str(l))
        elif comando[0] == "POST":
            l = listaSimples()
            t.PosOrdem(t.root,l)
            if l.fim == None:
                r.append("0")
            else:
                r.append(str(l))
    if caso == 1:
        print()
        print("Caso %i:"%caso)
    else:
        print("Caso %i:" % caso)
    for i in r:
        print(i)
    caso += 1