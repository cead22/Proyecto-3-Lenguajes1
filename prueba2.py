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

t11 =  T_funcion(T_var("a"),Int(4))
t12 =  T_funcion(T_var("v"),Int(4))
t21 =   T_funcion(T_var("b"), (T_funcion(T_var("c"),T_var("c"))))
t22 =   T_funcion(T_var("b"), (T_funcion(T_var("c"),T_var("c"))))

t31 =   T_funcion(T_var("b"), (T_funcion(T_var("x"),T_var("x"))))
t32 =   T_funcion(T_var("b1"),(T_funcion(T_var("x1"), (T_funcion(T_var("c"),T_var("c"))))))

printrec(unif(t31,t32))

#printrec(unif(i1,i2))
