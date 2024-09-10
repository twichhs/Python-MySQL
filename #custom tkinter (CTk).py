import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

import os
c=os.path.dirname(__file__)
nomeArquivo= c+"\\ctk_dados.txt"
def dados ():
        arquivo= open (nomeArquivo,"a")
        arquivo.write("Username:%s" % Username_teste.get())
        arquivo.write("\nSenha:%s" % PassWord_teste.get())
        arquivo.write('\n\n')
        arquivo.close()

janela =ctk.CTk()
janela.geometry("500x300")
# janela.configure(background="#252629")   
janela.title("Python CTK")

login_teste = ctk.CTkLabel(janela, text="Login", font=("arial",16))
login_teste.pack(padx=10, pady=10)
# no custom se coloca o width e o height junto com a variavél logo de cara. Porem tem uma forma mais pratica de ajustar a posição dos elementos
Username_teste = ctk.CTkEntry(janela, placeholder_text="Username")
Username_teste.pack(padx= 10 , pady= 10)

PassWord_teste = ctk.CTkEntry(janela, placeholder_text="Password", show="*")
PassWord_teste.pack(padx= 10 , pady= 10)

caixa = ctk.CTkCheckBox(janela, text= "Remember Me")
caixa.pack(padx= 10 , pady= 10)

BOTAO = ctk.CTkButton(janela, text="Enter", command=dados)
BOTAO.pack(padx= 10, pady= 10)


# botao = ctk.CTkButton()

janela.mainloop()



