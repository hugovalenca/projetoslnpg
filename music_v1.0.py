from tkinter import *
from tkinter.ttk import Combobox

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
    catalogo_albuns.write(f"{nome_album}%{ano_lancamento}%{nome_banda}%{primeiro_album}\n")
    catalogo_albuns.close()

# Função para exibir o conteúdo do bloco de notas gerado
def clicar_btn_mostrar():
    show = Toplevel()
    show.title("Music STORE & SHOW - Exibição")
    show.geometry("400x300")
    catalogo_albuns = open("catalogo_albuns.txt", "r", encoding="utf-8")
    albuns = catalogo_albuns.readlines()
    for album in albuns:
        album = album.split("%")
        Label(show, text=album).pack()
    catalogo_albuns.close()
    show.mainloop()

# Função para tela busca
def clicar_btn_procurar():
    search = Toplevel()
    search.title("Buscar Álbuns por Nome de Banda")
    search.geometry("400x300")
    Label(search, text="Digite o nome da Banda: ").place(x=40, y=130)
    Label(search, text="Álbuns: ").place(x=40, y=150)
    txtbox_buscar_album = Entry(search, text="")
    txtbox_buscar_album.place(x=190, y=130)
    # Função para procurar álbum
    def procurar_album():
        catalogo_albuns = open("catalogo_albuns.txt", "r", encoding="utf-8")
        albuns = catalogo_albuns.readlines()
        buscar_album = txtbox_buscar_album.get()
        for album in albuns:
            album = album.split("%")
            if buscar_album == album[2]:
                Label(search, text=album[0]).place(x=190, y=150)
            else:
                Label(search, text="Inexistente").place(x=190, y=150)
        catalogo_albuns.close()
    btn_buscar = Button(search, text="🔍", command=procurar_album)
    btn_buscar.pack()
    btn_buscar.place(x=330, y=126)
    search.mainloop()

# Função para buscar álbuns por ano
def clicar_btn_year():
    year = Toplevel()
    year.title("Buscar Álbuns por Ano")
    year.geometry("400x300")

    v1 = IntVar()
    v1.set(2)
    rdbtn1_year_anterior = Radiobutton(year, text="Anterior a", variable=v1, value=1)
    rdbtn2_year_igual = Radiobutton(year, text="Igual a", variable=v1, value=2)
    rdbtn3_year_posterior = Radiobutton(year, text="Posterior a", variable=v1, value=3)
    rdbtn1_year_anterior.place(x=80, y=80)
    rdbtn2_year_igual.place(x=170, y=80)
    rdbtn3_year_posterior.place(x=240, y=80)

    data = ("1990", "2000", "2010")
    cb = Combobox(year, values=data)
    cb.place(x=130, y=120)
    cb.current(1)


    catalogo_albuns = open("catalogo_albuns.txt", "r", encoding="utf-8")
    albuns = catalogo_albuns.readlines()
    for album in albuns:
        album = album.split("%")
    
    def pesquisar_ano():
        if v1.get() == 1 and cb.get() == "2010" and album[1] < "2010" and album[1] > "2000":
            Label(year, text=album[0]).place(x=190, y=150)
        elif v1.get() == 1 and cb.get() == "2000" and album[1] < "2000" and album[1] > "1990":
            Label(year, text=album[0]).place(x=190, y=150)
        elif v1.get() == 1 and cb.get() == "1990" and album[1] < "1990":
            Label(year, text=album[0]).place(x=190, y=150)
        elif v1.get() == 2 and cb.get() == "2010" and album[1] == "2010":
            Label(year, text=album[0]).place(x=190, y=150)
        elif v1.get() == 2 and cb.get() == "2000" and album[1] == "2000":
            Label(year, text=album[0]).place(x=190, y=150)
        elif v1.get() == 2 and cb.get() == "1990" and album[1] == "1990":
            Label(year, text=album[0]).place(x=190, y=150)
        elif v1.get() == 3 and cb.get() == "1990" and album[1] > "1990" and album[1] < "2000":
            Label(year, text=album[0]).place(x=190, y=150)
        elif v1.get() == 3 and cb.get() == "2000" and album[1] > "2000" and album[1] < "2010":
            Label(year, text=album[0]).place(x=190, y=150)
        elif v1.get() == 3 and cb.get() == "1990" and album[1] > "2010":
            Label(year, text=album[0]).place(x=190, y=150)
        else:
            Label(year, text="Nenhum álbum foi encontrado").place(x=190, y=150)


    btn_year_pesquisar = Button(year, text="🔍", command=pesquisar_ano)
    btn_year_pesquisar.pack()
    btn_year_pesquisar.place(x=110, y=200)

    catalogo_albuns.close()

    year.mainloop()

# Criação da janela
window = Tk()
window.title("Music STORE & SHOW - Registro")
window.geometry("400x300")

# Nome do álbum
Label(window, text="Nome do álbum: ").place(x=70, y=40)
txtbox_nome_album = Entry(window, text="")
txtbox_nome_album.place(x=210, y=40)

# Ano de lançamento
Label(window, text="Ano de lançamento: ").place(x=70, y=90)
txtbox_ano_lancamento = Entry(window, text="")
txtbox_ano_lancamento.place(x=210, y=90)

# Nome da banda/artista
Label(window, text="Nome da banda/artista: ").place(x=70, y=140)
txtbox_nome_banda = Entry(window, text="")
txtbox_nome_banda.place(x=210, y=140)

# É o primeiro álbum?
Label(window, text="É o primeiro álbum?").place(x=70, y=190)
v0 = IntVar()
v0.set(2)
rdbtn1_primeiro_album = Radiobutton(window, text="Sim", variable=v0, value=1)
rdbtn2_primeiro_album = Radiobutton(window, text="Não", variable=v0, value=2)
rdbtn1_primeiro_album.place(x=210, y=190)
rdbtn2_primeiro_album.place(x=260, y=190)

# Botão para registrar
btn_registrar = Button(window, text="STORE", command=clicar_btn_registrar)
btn_registrar.pack()
btn_registrar.place(x=110, y=240)

# Botão para mostrar
btn_mostrar = Button(window, text="SHOW", command=clicar_btn_mostrar)
btn_mostrar.pack()
btn_mostrar.place(x=170, y=240)

# Botão para procurar álbuns
btn_mostrar = Button(window, text="SEARCH", command=clicar_btn_procurar)
btn_mostrar.pack()
btn_mostrar.place(x=230, y=240)

# Botão para procurar álbuns por ano
btn_mostrar = Button(window, text="YEAR", command=clicar_btn_year)
btn_mostrar.pack()
btn_mostrar.place(x=300, y=240)

# Finalização da janela
window.mainloop()