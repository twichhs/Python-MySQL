from tkinter import *
import os
c=os.path.dirname(__file__)

nomeArquivo= c+"\\dados.txt"
yn=input("Open interface S/N?")
if yn == "S":
    def dados ():
        arquivo= open (nomeArquivo,"a")
        arquivo.write("Nome...:%s" % enome.get())
        arquivo.write("\nTelefone...:%s" % efone.get())
        arquivo.write("\nEmail...:%s" % email.get())
        arquivo.write("\nCPF...:%s" % ecpf.get())
        arquivo.write('\n\n')
        arquivo.close()


    login = Tk()
    login.title("Pagina de Login")
    login.configure(background="#4d5243")
    login.geometry('500x500')
    Label(login, text= 'Nome',background="#4d5243", font=("arial",13)).place(x=200, y=10, width=80, height=20)
    enome=Entry(login)
    enome.place(x=160, y=40, width=170, height=20)
    Label(login, text="Email",background="#4d5243", font=("arial",13)).place(x=200, y=70, width=80, height=20)
    # modelos : 
    # Label(login, text="Email",background="#4d5243", font=("arial",14)).place(x=200, y=70, width=80, height=20)
    # enome=Entry(login)
    # enome.place(x=160, y=40, width=170, height=20)
    email=Entry(login)
    email.place(x=160, y=100, width=170, height=20)
    Label(login, text="Telefone",background="#4d5243", font=("arial",13)).place(x=200, y=130, width=80, height=20)
    efone=Entry(login)
    efone.place(x=160, y=160, width=170, height=20)
    Label(login, text="CPF",background="#4d5243", font=("arial",13)).place(x=200, y=190, width=80, height=20)
    ecpf=Entry(login)
    ecpf.place(x=160, y=220, width=170, height=20)
    Button(login,command=dados,text='Cadastrar',background="#737d75",font=("arial",13)).place(x=143, y=400, width=200, height=40)


    login.mainloop()
else:
    print("No problem, see you son!")
