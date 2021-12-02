contX=0
aim=0
contAux=0
depth=0

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
            depth+=y_datos[contAux]*aim
            contAux+=1
        if(lineaAux=='down'):
            aim+=y_datos[contAux]
            contAux+=1
        if(lineaAux=='up'):
            aim-=y_datos[contAux]
            contAux+=1
    print(contX*depth)
    
