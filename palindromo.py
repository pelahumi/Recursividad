def palindromo(palabra):
    if len(palabra) < 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return palindromo(palabra[1 : -1])
        else:
            return False

palabra = str(input("Introduce una palabra: "))
palindromo(palabra)
