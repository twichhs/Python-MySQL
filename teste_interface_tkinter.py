from tkinter import *

# Criação da janela principal
janela = Tk()
janela.title("Calculadora do 2º grau")
janela.geometry('500x300')
janela.configure(background="#f5f5dc")

# Mantém a janela aberta
janela.mainloop()







#grid serve pra mudar a posição das coisas
#deixar o mainloop na ultima linha do tk inter
janela.mainloop() #ele diz para o progama para continuar exibindo nossa janela, mesmo que o código acabe
coeficientes = Label(janela, text='Ola ')
coeficientes.grid(column=0, row=3)
