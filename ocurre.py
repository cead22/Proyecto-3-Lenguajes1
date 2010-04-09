from analizador import *

x,y,z,w,q = T_var('x'), T_var('y'), T_var('z'), T_var('w'),T_var('q')
yz, yx, xy, xq, qx, wz, zq, qw = T_funcion(y,z), T_funcion(y,x), T_funcion(x,y),T_funcion(x,q), T_funcion(q,x), T_funcion(w,z), T_funcion(z,q), T_funcion(q,w)

pyz, pyx, pxy = T_parentesis(yz),T_parentesis(yx),T_parentesis(xy)
f1 = T_funcion(T_funcion(T_parentesis(zq),T_parentesis(T_funcion(qx,T_parentesis(T_funcion(qw,y))))),wz)

print ocurre(x,yz), ocurre(x,yx), ocurre(x,xy)
print ocurre(x,pyz), ocurre(x,pyx), ocurre(x,pxy)
print f1, ocurre(T_var('h'),f1)
