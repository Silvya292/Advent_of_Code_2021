contX=0
contY=0
contAux=0

with open('inputDay2.txt','r') as f:
    x_datos=[]
    y_datos=[]
    lineas=f.readlines()
    for linea in lineas:
        x,y=linea.split()
        x_datos.append(x)
        y_datos.append(int (y))
    
    for lineaAux in x_datos:
        if(lineaAux=='forward'):
            contX+=y_datos[contAux]
            contAux+=1
        if(lineaAux=='down'):
            contY+=y_datos[contAux]
            contAux+=1
        if(lineaAux=='up'):
            contY-=y_datos[contAux]
            contAux+=1
    print(contX*contY)