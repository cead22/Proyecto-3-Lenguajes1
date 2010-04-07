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

#    def __init__(self):
#        self.t = 'Tipo'

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


def componer(s1,s2):
    res = []
    for s in s1:
        x1 = s[0]
        t1 = s[1]
        res = res + [(x1,sustituir(s2,t1))]
    return res

def printrec(lista):
    print '[',
    for l1 in lista:
        print '(', l1[0] , ',' , l1[1],  '),',
    print ']',

#def sin_parentesis(p):
    

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
        if isinstance(t2,Int):
            if t1.t == t2.t: return []
            else: raise 'No Unifica (1)'
        else: raise 'No Unifica (2)'

    # t1 es booleano, solo unifica con el mismo
    if isinstance(t1,Bool):
        if isinstance(t2,Bool) and t1.t == t2.t: return []
            else: raise 'No Unifica (3)'
        else: raise 'No Unifica (4)'

    # t1 es funcion
    '''
    if isinstance(t1,T_funcion):
        if isinstance(t2,T_funcion):
            temp = unif(t1.dominio,t2.dominio)
            temp = temp + unif(t1.rango,t2,rango)
            return temp
        else: raise 'No Unifica (5)'
            
'''
