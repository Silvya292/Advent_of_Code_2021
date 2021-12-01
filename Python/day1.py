f = open("inputDay1.txt", "r")

cont=1
linea = f.readline()

while linea != "":
    lineaAux = f.readline()

    if (lineaAux>linea):
        cont+=1

    linea=lineaAux

print(cont)
f.close()