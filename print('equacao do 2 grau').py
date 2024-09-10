a= float(input("Digite o valor do coeficiente a: "))
b= int(input("Digite o valor do coeficiente b: "))
c= int(input("Digite o valor do coeficiente c: "))
delta = b**2 - 4*a*c
print('O valor de delta é',delta)
x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)
print(x1)
print(x2)