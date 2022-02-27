# Recursividad
La dirección de este repositorio es la siguuiente: [GitHub](https://github.com/pelahumi/Recursividad)

## Búsqueda por dicotomía
```python
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
```

## Palíndromos
```python
def caracteres_especiales(palabra):
    
    #Esta función nos elimina los posibles acentos y suprime los espacios
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")

    return palabra

def palindromo(palabra):

    #Este condicional nos devuelve True si la palabra es palíndroma y False en caso contrario

    if len(palabra) < 1:
        return True
    else:
        #Este condicional va comparando la primera palabra con la última para comprobar si son iguales
        
        if palabra[0] == palabra[-1]:
            return palindromo(palabra[1 : -1])
        else:
            return False

palabra = str(input("Introduce una palabra: "))
print("La palabra ", palabra, " es palíndromo: ", palindromo(caracteres_especiales(palabra)))
``