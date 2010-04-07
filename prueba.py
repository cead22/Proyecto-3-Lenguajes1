#!/usr/bin/python

from analizador import *


a = T_var('a')
print a

b = T_var('b')
print b

btobool = T_funcion(b,Bool())
print btobool

atob = T_funcion(a,b)
print atob

atoa = T_funcion(a,a)
print atoa


print remplazar(a,btobool,atob)

print remplazar(a,btobool,atoa)

print sustituir([(a,btobool)],atob)

print sustituir([(b,T_var('c'))],sustituir([(a,btobool)],atob))

print sustituir([(a,btobool),(b,T_var('c'))], atob)

print sustituir([(b,a)],T_parentesis(b))
