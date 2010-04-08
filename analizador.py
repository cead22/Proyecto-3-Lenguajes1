#! /usr/bin/python

from pylog import *


# Expresiones

class Expresion:

    def __init__(self,i):
        self.izq = i

class Entero(Expresion): pass
class Booleano(Expresion): pass
class E_var(Expresion): pass
class E_parentesis(Expresion): pass

class ExpresionBinaria(Expresion):

    def __init__(self,i,d):
        self.izq = i
        self.der = d

class Suma(ExpresionBinaria): pass
class Menor(ExpresionBinaria): pass
class Conjuncion(ExpresionBinaria): pass
class Aplicacion(ExpresionBinaria): pass
class E_funcion(ExpresionBinaria): pass


# Tipos 
class Tipo:

    def __init__(self):
        #pass
        self.t = 'Tipo'

    def __init__(self,t):
        self.t = t

    def __str__(self):
        return str(self.t)

class Int(Tipo): pass

#    def __init__(self):
#        self.t = 'int'

class Bool(Tipo): pass

#    def __init__(self):
#        self.t = 'bool'

class T_var(Tipo): 

#    def __init__(self,t):
#        self.t = t

    def __str__(self):
        return str(self.t)

class T_parentesis(Tipo):

    def __init__(self,t):
        self.t = t

    def __str__(self):
        return '(' + str(self.t) + ')'

class T_funcion(Tipo):

    def __init__(self,d,r):
        self.t = None
        self.dominio = d # dominio
        self.rango = r # rango

    def __str__(self):
        return str(self.dominio) + '-->' + str(self.rango)

def sustituir(lista,tipo):
    for tupla in lista:
        tipo = remplazar(tupla[0],tupla[1],tipo)
    return tipo
        
# var es T_var
# tipo es Tipo
# tipo_destino es Tipo
def remplazar(var,tipo,tipo_destino):
    
    # misma variable de tipo que tipo ej: (a,a,a-->int)
    if var.t == tipo.t: return tipo_destino

    # caso parentesis
    if isinstance(tipo_destino,T_parentesis):
        return T_parentesis(remplazar(var,tipo,tipo_destino.t))

    # si el tipo destino no es funcion (caso base)
    if not isinstance(tipo_destino,T_funcion):
        if var.t == tipo_destino.t: return T_parentesis(tipo)
        return tipo_destino

    # caso recursivo, se remplaza en dominio y en rango
    dom = remplazar(var,tipo,tipo_destino.dominio)
    ran = remplazar(var,tipo,tipo_destino.rango)
    return T_funcion(dom,ran)


# Retorna todos los pares (x1,T1) de s1 y todos
# los pares (x2,T2) de s2 tales que x2 no sea ningun
# x1 de s1
def restar(s1,s2):
    res = []
    for par2 in  s2:
        for par1 in s1:
            if not (par2[0] == par1[0]):
                res = res + [par2]
    return res

# Retorna la sustitucion que resulta de componer
# las sustituciones s1 con s2
def componer(s1,s2):
    res = restar(s1,s2)
    for s in s1:
        x1 = s[0]
        t1 = s[1]
        res = res + [(x1,sustituir(s2,t1))]
    return res

# Imprime listas de tuplas de tipos
def printrec(lista):
    print '[',
    for l1 in lista:
        print '(', l1[0] , ',' , l1[1],  '),',
    print ']',


# Unificacion sin revision de ocurrencia
def unif(t1,t2):
    
    # t1 entre parentesis
    if isinstance(t1,T_parentesis): return unif(t1.v,t2)

    # t2 entre parentesis
    if isinstance(t2,T_parentesis): return unif(t1,t2.v)

    # t1 es variable, unifica con todo
    if isinstance(t1,T_var): return [(t1,t2)]

    # t2 es variable, unifica con todo
    if isinstance(t2,T_var): return [(t2,t1)]

    # t1 es entero, solo unifica con el mismo
    if isinstance(t1,Int):
        if isinstance(t2,Int): return []
        else: raise 'No Unifica (2)'

    # t1 es booleano, solo unifica con el mismo
    if isinstance(t1,Bool):
        if isinstance(t2,Bool): return []
        else: raise 'No Unifica (3)'

    # t1 es funcion
    if isinstance(t1,T_funcion):
        if isinstance(t2,T_funcion):
            temp = unif(t1.dominio,t2.dominio)
            aux1 = sustituir(temp,t1.rango)
            aux2 = sustituir(temp,t2.rango)
            return componer(temp,unif(aux1,aux2))
        else: raise 'No Unifica (4)'
    
    else: raise 'No Unifica (Falta Algun Caso)'
    

def extender

def amb(env,exp):
    
    # Entero
    if isinstace(exp,Entero): return Int(exp.izq)
    
    # Booleano
    if isinstace(exp,Booleano): return Bool(exp.izq)
   
    # Variable
    if isinstace(exp,E_var):
        for a in env:
            if a[0] == exp: return a[1]
        raise 'Error (a)'
    
    # Suma o Menor
    if isinstace(exp,Suma) || isinstance(exp,menor):
        if isinstance(amb(env,exp.izq),Int) && isinstance(amb(env,exp.der),Int): 
            return Int()
        raise 'Error (b)'
    
    # Conjuncion
    if isinstace(exp,Conjuncion):
        if isinstance(amb(env,exp.izq),Bool) && isinstance(amb(env,exp.der),Bool): 
            return Int()
        raise 'Error (c)'

    # Funcion
    if isinstace(exp,E_funcion):
        t1 = amb(env,exp.izq)
        t2 = amb(env,exp.der)
        return T_funcion(t1,t2)

    # Aplicacion
    if isinstace(exp,Aplicacion):
        e1 = exp.izq
        e2 = exp.der
        a1 = amb(env,e1)
        if isinstance(a1,T_funcion) && amb(env,e1) == a1.domino:
            return a1.rango
        raise 'Error (d)'
            
