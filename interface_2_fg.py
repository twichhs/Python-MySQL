from tkinter import *

def calculadora():
 try:
    a= int(entry_a.get()) 
    b= int(entry_b.get())
    c= int(entry_c.get())

    delta = b**2 - 4*a*c
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    xv = (-b) / (2*a)
    yv = (- delta) / (4*a)
    eixoY = c

    label_x1.config(text=f'X1 = {x1:.2f}')
    label_x2.config(text=f'X2 = {x2:.2f}')
    label_xv.config(text=f'XV = {xv:.4f}')
    label_yv.config(text=f'YV = {yv:.4f}')
    label_eixoY.config(text=f'O eixo Y é: {eixoY}')
    label_delta.config(text=f'O delta é {delta}')
 except ValueError:
    Label(app,text='Preencha todos os coeficientes com números',foreground='#FF0000',background="#fff9cc").place(x=120,y=450,width=240,height=20)

#se não der certo com float vou pro int mesmo kkkkk
#alias, se pra voce % estiver em int siginifica que eu coringuei mesmo
app= Tk()
app.title("Calculadora do 2º grau")
app.geometry('500x500')
app.configure(background="#fff9cc")
#anchor representa as direções como S=sul-N=norte, E=leste, W=oeste
#app_espace= Label(app, text=' ')
Label(app, text="Digite os coeficientes",foreground="#009",background="#fff9cc",font=('arial',11)).place(x=160,y=10,width=150,height=20)
Label(app, text='Coeficiente a',foreground="#009",background="#fff9cc",font=('arial',11)).place(x=160,y=60,width=150,height=20)
entry_a=Entry(app)
entry_a.place(x=160,y=80,width=150,height=20)
Label(app, text="Coeficiente b",foreground="#009",background="#fff9cc",font=('arial',11)).place(x=160,y=120,width=150,height=20)
entry_b=Entry(app)
entry_b.place(x=160,y=140,width=150,height=20)
Label(app, text="Coeficiente c",foreground="#009",background="#fff9cc",font=('arial',11)).place(x=160,y=180,width=150,height=20)
entry_c=Entry(app)
entry_c.place(x=160,y=200,width=150,height=20)
Button(app, text='calcular', command=calculadora,foreground="#006400",background="#fff9cc",font=("arial",11)).place(x=160,y=240,width=150,height=20 )
#aqui ficam as variaveis que serão formatadas na função e exibiram a resposta
label_x1 = Label(app, text="", foreground="#000", background="#fff9cc", font=('arial',11))
label_x1.place(x=160,y=280,width=150,height=20)
label_x2 = Label(app, text="", foreground="#000", background="#fff9cc", font=('arial',11))
label_x2.place(x=160,y=300,width=150,height=20)
label_xv = Label(app, text="", foreground="#000", background="#fff9cc", font=('arial',11))
label_xv.place(x=160,y=320,width=150,height=20)
label_yv = Label(app, text="", foreground="#000", background="#fff9cc", font=('arial',11))
label_yv.place(x=160,y=340,width=150,height=20)
label_eixoY = Label(app, text="", foreground="#000", background="#fff9cc", font=('arial',11))
label_eixoY.place(x=160,y=360,width=150,height=20)
label_delta = Label(app, text="", foreground="#000", background="#fff9cc", font=('arial',11))
label_delta.place(x=160,y=380,width=150,height=20)

app.mainloop()