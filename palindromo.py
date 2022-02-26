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
print("La palabra ", palabra, " es palíndromo: ", palindromo(palabra))
