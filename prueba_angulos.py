import math

def distancia(x,y,i):
    """
    Recibe dos puntos y calcula su distancia
    """
    return math.sqrt(((x[i+1]-x[i])**2)+((y[i+1]-y[i])**2))
def angulo(x,y,i):
    """
    Calcula el angulo entre el vector formado por dos puntos 
    y la horizontal (X)
    """
    V_u = [1,0]
    V = [x[i+1]-x[i],y[i+1]-y[i]] 
    angu = math.degrees(math.acos(((V[0]*V_u[0])+(V[1]*V_u[1]))/(math.sqrt(((V[0])**2)+((V[1])**2))*math.sqrt(((V_u[0])**2)+((V_u[1])**2)))))
    return angu



lista = [(0,0),(1,1),(2,1),(2,2),(3,4),(1,1)]
listaDis,listaAngu = [],[]
x,y = zip(*lista)
c = len(x)

for i in range(0,c-1):
    listaDis.append(distancia(x,y,i))
    listaAngu.append(angulo(x,y,i))
    
listafinal = zip(listaDis,listaAngu)
print(*listafinal)













