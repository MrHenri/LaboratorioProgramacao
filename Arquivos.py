def merge(a,b):
    lista = []
    aI, bI = 0,0
    while aI < len(a) and bI < len(b):
        if a[aI] > b[bI]:
            lista.append(a[aI])
            aI+=1
        else:
            lista.append(b[bI])
            bI+=1
    if aI == len(a):
        lista.extend(b[bI:])
    else:
        lista.extend(a[aI:])
    return lista

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = int(len(a)/2)
    e, d = merge_sort(a[:mid]), merge_sort(a[mid:])
    return merge(e,d)

n, b = map(int, input().split())
lista = list(map(int, input().split()))
lista = merge_sort(lista)
c = 0
i = 0
while lista[i] == b:
    c+=1
    i+=1
j = n-1
while lista[i] != None or lista[j] != None:
    if lista[i] + lista[j] > b:
        c+=1
        lista[i] = None
        i+=1
    else:
        c+=1
        lista[i] = None
        lista[j] = None
        i+=1
        j-=1
print(c)

