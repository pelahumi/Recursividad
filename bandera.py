fichas = ["V", "A", "V", "V", "R", "A", "A", "R"]
bandera_ordenada = []

def bandera(n, fichas):

    if n <= (len(fichas) - 1):

        if fichas[n] == "V":
            bandera_ordenada.append("V")

        elif fichas[n] == "A":
            bandera_ordenada.append("A")
        
        elif fichas[n] == "R":
            bandera_ordenada.append("R")

        bandera(n + 1, fichas)

    else:
        print("La bandera está ordenada")

bandera(0, fichas)
print(bandera_ordenada)