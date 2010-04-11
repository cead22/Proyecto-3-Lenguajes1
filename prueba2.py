from analizador import *
'''
from analizador import T_funcion

s1 = [(T_var("a"),T_var("b"))]
s2 = [(T_var("b"),T_funcion(T_var("d"),T_var("e")))]
c = componer(s1,s2)
printrec([(T_funcion(T_var("d"),T_var("e")),5)])

print ''

i1 = Int(5)
i2 = Int(6)
f = T_funcion(T_var("d"),T_var("e"))

<<<<<<< HEAD:prueba2.py
t11 =  T_funcion(T_var("a"),Int(4))
t12 =  T_funcion(T_var("v"),Int(4))
t21 =   T_funcion(T_var("b"), (T_funcion(T_var("c"),T_var("c"))))
t22 =   T_funcion(T_var("b"), (T_funcion(T_var("c"),T_var("c"))))

t31 =   T_funcion(T_var("b"), (T_funcion(T_var("x"),T_var("x"))))
t32 =   T_funcion(T_var("b1"),(T_funcion(T_var("x1"), (T_funcion(T_var("c"),T_var("c"))))))

printrec(unif(t31,t32))

#printrec(unif(i1,i2))
=======
printrec(unif(i1,i2))

print ''
print  '---------------'

'''
x = E_var('x')
a = T_var('a')
s1 = [(x,a)]
s = lambda z: T_var('a') if z == x else vacio
def Amb(exp):
    #print 'bbb' ,exp
    if isinstance(exp,E_var) and exp.izq == 'x': return T_var('y')
    if isinstance(exp,Entero): return Int(exp.izq)
    if isinstance(exp,Booleano): return Bool(exp.izq)
    return vacio
uno = Entero(1)

#print s(x).__class__

res=asigTipo(Amb,E_funcion(x,x),T_var('h'))
print res[1][1]
printrec(res)

