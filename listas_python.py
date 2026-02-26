lista1=list()
lista2=[]
print(type(lista1))
print(type(lista2))
lista1.append(100)
lista1.append(4.5)
lista1.append([])

class nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
a=nodo(100)
b=nodo(1000)
c=nodo(1)
d=nodo(10)

a.siguiente=b
b.siguiente=c
c.siguiente=d
d.siguiente=None

actual=a
while actual.siguiente:
    print(actual.dato)
    actual=actual.siguiente