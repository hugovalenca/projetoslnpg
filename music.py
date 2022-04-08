from tkinter import *

# Função para ler os conteúdos das caixas de texto
def clicar_btn_registrar():
    nome_album = txtbox_nome_album.get()
    txtbox_nome_album.delete(0, 'end')
    ano_lancamento = txtbox_ano_lancamento.get()
    txtbox_ano_lancamento.delete(0, 'end')
    nome_banda = txtbox_nome_banda.get()
    txtbox_nome_banda.delete(0, 'end')
    catalogo_albuns = open("catalogo_albuns.txt", "a", encoding="utf-8")
    if (v0.get() == 1):
        primeiro_album = "Sim"
    else:
        primeiro_album = "Não"
    dados_album = nome_album + " " + ano_lancamento + " " + nome_banda + " " + primeiro_album
    catalogo_albuns.write(f'{dados_album}\n')
    catalogo_albuns.close()

# Função para exibir o conteúdo do bloco de notas gerado
def clicar_btn_mostrar():
    show = Toplevel()
    show.title("Music STORE & SHOW - Exibição")
    show.geometry("400x300")
    catalogo_albuns = open("catalogo_albuns.txt", "r", encoding="utf-8")
    albuns = catalogo_albuns.readlines()
    for album in albuns:
        Label(show, text=album).pack()
    catalogo_albuns.close()
    show.mainloop()

# Criação da janela
window = Tk()
window.title("Music STORE & SHOW - Registro")
window.geometry("500x600")

# Nome do álbum
Label(window, text="Nome do álbum: ").place(x=50, y=150)
txtbox_nome_album = Entry(window, text="")
txtbox_nome_album.place(x=190, y=150)

# Ano de lançamento
Label(window, text="Ano de lançamento: ").place(x=50, y=200)
txtbox_ano_lancamento = Entry(window, text="")
txtbox_ano_lancamento.place(x=190, y=200)

# Nome da banda/artista
Label(window, text="Nome da banda/artista: ").place(x=50, y=250)
txtbox_nome_banda = Entry(window, text="")
txtbox_nome_banda.place(x=190, y=250)

# É o primeiro álbum?
Label(window, text="É o primeiro álbum?").place(x=50, y=300)
v0 = IntVar()
v0.set(2)
rdbtn1_primeiro_album = Radiobutton(window, text="Sim", variable=v0, value=1)
rdbtn2_primeiro_album = Radiobutton(window, text="Não", variable=v0, value=2)
rdbtn1_primeiro_album.place(x=190, y=300)
rdbtn2_primeiro_album.place(x=240, y=300)

# Botão para registrar
btn_registrar = Button(window, text="STORE", command=clicar_btn_registrar)
btn_registrar.pack()
btn_registrar.place(x=190, y=350)

# Botão para mostrar
btn_mostrar = Button(window, text="SHOW", command=clicar_btn_mostrar)
btn_mostrar.pack()
btn_mostrar.place(x=250, y=350)

# Finalização da janela
window.mainloop()
