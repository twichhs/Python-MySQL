'''
x = 30 
y = 90
if y % x  == 2:
    print("90 é dividivel por 30")
else:
    print("Numero quebrado")
'''
def sub(x , y):
    return x-y

def subs(x , y):
    print(x - y)
'''
resultado1= sub(4 , 4554) 
resultado2= sub(4 , 6)

print("sem return : " ,resultado1)
print("com return:" ,resultado2)

print("Diretamente no print sem return: ", subs(30,10))
print("Diretamente no print com return: ", sub(34, 12))
# no fim, isto prova a superioridade do return, simplesmente o return
'''
def happy_birthday(name , age):
    print(f"Happy bithday to you {name} !")
    print(f"You are {age} years old")
    print(f"I will always love you {name}")


# happy_birthday("Pedro" , 11)

def return_fullname(name, lastname):
    name.capitalize()
    lastname.capitalize()
    return name + " " + lastname

print(return_fullname("Leonardo" , "Cunha"))

