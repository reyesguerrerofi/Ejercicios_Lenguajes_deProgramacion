class A:  
    def __init__(self, x = 10, y = 5): #Cuando una clase define un método __init__(), la instanciación 
        self._x = x                    #de la clase automáticamente invoca a __init__() para la instancia 
        self._y = y                    #recién creada. 
    def obten(self):                   #Fuente: http://docs.python.org.ar/tutorial/3/classes.html
        return self._x,self._y
class B(A):
    def __init__(self,z = 2): #Encadenamiento explicito, de no hacerse el metodo suma no podria realizarse
        A.__init__(self)        
        self._z = z
    def suma(self):
        sum = self._x + self._y + self._z
        return sum
class C(B):
    def __init__(self, w = 3): #Encadenamiento explicito, de no hacerse el metodo multiplicacion no podria realizarse
        A.__init__(self)       
        B.__init__(self)
        self._w = w
    def multiplica(self):
        mult = self._x * self._y * self._z * self._w
        return mult
c = C()
print(c.multiplica())
print(c.suma())
e = C(5)
print(e.multiplica())
t = B(5)
print(t.suma())
v = A(50,60)
print(v.obten())



