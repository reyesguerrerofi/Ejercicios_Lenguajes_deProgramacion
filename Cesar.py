def Encripta(Mensaje): #Se necesita una funcion para guardar el texto
    """
    La funcion regresa el mensaje cifrado (sin espacios)
    >>>K = 1 #Desplazamiento
    >>>Mensaje = [LACRIPTOGRAFIAESROMANTICA]
    >>>[MBDSJQUPHSBGJBFTSPNBÑUJDB]
    """
    k = int(input("Desplazamiento: "))
    n = len(Mensaje)
    ind = IndiceN(Mensaje) #Para cifrar el mensaje se usa de referencia los indices de la lista que lo contiene, esta funcion regresa los indices "cifrados"
    indicescif = []
    print(ind)
    for i in range(0,n):
        indicescif.append((ind[i]+k)% 28) #Usa la formula para cifrar los mensajes 
    mensajeci = IndiceE(indicescif)
    
    return 0        
    #Le falta la variante que se pide en clase































