f = open("inputDay1.txt", "r")

res=0
lista=[]

for linea in f:
    n=int(linea)
    lista.append(n)

for index,current in enumerate(lista):                                
    if(index>2):                                          
        suma1=lista[index-3]+lista[index-2]+lista[index-1]      
        suma2=lista[index-2]+lista[index-1]+current  
        if(suma1<suma2):                            
            res+=1

print(res)
f.close()