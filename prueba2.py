from analizador import *

from analizador import T_funcion

s1 = [(T_var("a"),T_var("b"))]
s2 = [(T_var("b"),T_funcion(T_var("d"),T_var("e")))]
c = componer(s1,s2)
printrec([(T_funcion(T_var("d"),T_var("e")),5)])

print ''

i1 = Int(5)
i2 = Int(6)
f = T_funcion(T_var("d"),T_var("e"))

printrec(unif(i1,i2))
