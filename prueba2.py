from analizador import *

# entero
uno = Entero(1)

# booleano
true = Booleano('true')

# var
x = E_var('x')
y = E_var('y')


# (E)
paren = E_parentesis(x)

# E1 + E2
suma = Suma(x,y)

# E1 < E2
menor = Menor(x,y)

# E1 ^ E2
conj = Conjuncion(x,y)

# lambda var.E
fun1 = E_funcion(x,x) # lambda x.x
fun2 = E_funcion(x,Suma(x,uno)) # lamba x.(x+1)
fun3 = E_funcion(x,Conjuncion(x,true)) # lamba x.(x ^ true)

# E1 E2
apl = Aplicacion(fun2,x)

# Variables de tipo
i = T_var('i')
b = T_var('b')


# Ambiente con [(x,i)]
def Amb_1(exp):
    if isinstance(exp,E_var) and exp.izq == 'x': return i
    return vacio

# Ambiente con [(x,i),(y,i)]
def Amb_2(exp):
    if isinstance(exp,E_var) and exp.izq == 'x': return i
    if isinstance(exp,E_var) and exp.izq == 'y': return i
    return vacio

# Ambiente con [(x,b),(y,b)]
def Amb_3(exp):
    if isinstance(exp,E_var) and exp.izq == 'x': return b
    if isinstance(exp,E_var) and exp.izq == 'y': return b
    return vacio

# Ambiente con [(x,i),(y,b)]
def Amb_4(exp):
    if isinstance(exp,E_var) and exp.izq == 'x': return i
    if isinstance(exp,E_var) and exp.izq == 'y': return b
    return vacio

# Tipo de la expresion '1'
res1 = asigTipo(Amb_1,uno,T_var('r'))
print 'Tipo de la expresion \'1\''
printrec(res1)
print '\n'

# Tipo de la expresion 'true'
res2 = asigTipo(Amb_1,true,T_var('r'))
print 'Tipo de la expresion \'true\''
printrec(res2)
print '\n'

# Tipo de la expresion 'x'
res3 = asigTipo(Amb_1,x,T_var('r'))
print 'Tipo de la expresion \'x\''
printrec(res3)
print '\n'

# Tipo de la expresion '(x)'
res4 = asigTipo(Amb_1,paren,T_var('r'))
print 'Tipo de la expresion \'(x)\''
printrec(res4)
print '\n'

# Tipo de la expresion 'x + y'
res5 = asigTipo(Amb_2,suma,T_var('r'))
print 'Tipo de la expresion \'x + y\''
printrec(res5)
print '\n'
 
# Tipo de la expresion 'x < x'
res6 = asigTipo(Amb_2,menor,T_var('r'))
print 'Tipo de la expresion \'x < y\''
printrec(res6)
print '\n'

# Tipo de la expresion 'x ^ true'
res7 = asigTipo(Amb_3,conj,T_var('r'))
print 'Tipo de la expresion \'x ^ true\''
printrec(res7)
print '\n'

# Tipo de la expresion 'x ^ true'
res7 = asigTipo(Amb_4,conj,T_var('r'))
print 'Tipo de la expresion \'x ^ true\''
print '(misma prueba anterior pero con x de tipo i'
print 'la salida indica que el tipo i debe ser equivalente a bool)'
printrec(res7)
print '\n'


# Tipo de la expresion 'f' (funcion)
res8 = asigTipo(Amb_1,fun1,T_var('r'))
print 'Tipo de la expresion \'fun\' con fun::a --> a, fun x = x'
printrec(res8)
print 'con T_funcion ::',str(res8[0][1])
print '\n'


# Tipo de la expresion 'f' (funcion)
res9 = asigTipo(Amb_1,fun2,T_var('r'))
print 'Tipo de la expresion \'fun\' con fun::a --> a, fun x = x+1'
printrec(res9)
print 'con T_funcion ::',str(res9[0][1])
print '\n'


# Tipo de la expresion 'f' (funcion)
res10 = asigTipo(Amb_3,fun3,T_var('r'))
print 'Tipo de la expresion \'fun\' con fun::a --> a, fun x = x^true'
printrec(res10)
print 'con T_funcion ::',str(res10[0][1])
print '\n'


# Tipo de la expresion 'f x' (funcion)
res11 = asigTipo(Amb_1,apl,T_var('r'))
print 'Tipo de la expresion \'fun x\' con fun::a --> a, fun x = x+1'
printrec(res11)
print '\n'
