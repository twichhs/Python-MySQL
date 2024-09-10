# com a função de 2° podemos procurar no xv e o yv
# achar as raizes
a= float(input("Digite o valor do coeficiente a: ")) #float é usado para números quebrados
b= int(input("Digite o valor do coeficiente b: "))
c= int(input("Digite o valor do coeficiente c: "))
print( type(a))
delta = b**2 - 4*a*c
print('O valor de delta é',delta)
x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)
xv = (-b) / (2*a)
yv = (- delta) / (4*a)
eixoY = c
print("X1 e igual a : ",x1)
print("X2 e igual a : ",x2)
print('O x do vertice é igual a: ', xv)
print('O y do vertice é igual a: ',yv)
print('O eixo Y é:',eixoY)