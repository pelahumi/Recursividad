lista = [13, 45, 23, 98, 27, 37, 77, 1, 63]

def ordenar(lista):
    #Lo primero ordenamos la lista de menor a mayor
    lista.sort()
    #Nos devuelve la lista ordenada
    return lista

def busqueda(n, lista):

    if len(lista) == 0:
        print("No existe el número que buscas")
      
    mid = len(lista) // 2

    #Busca desde la mitad de la lista a la derecha
    if n > lista[mid]:
        lista = lista[mid + 1:]
        busqueda(n, lista)
    
    #Busca hacia la izquierda
    elif n < lista[mid]:
        lista = lista[:mid]
        busqueda(n, lista)
    
    else:
        print("Encotrado")

print(lista)
print("Introduce un número de la lista:")
n = int(input())
ordenar(lista)
busqueda(n, lista)