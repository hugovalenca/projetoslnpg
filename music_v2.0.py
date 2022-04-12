from tkinter import *
from tkinter import ttk
import tkinter

# Função para ler os conteúdos das caixas de texto e registrá-los no bloco de notas
dados_album_juntos = []
catalogo_albuns = open("catalogo_albuns.txt", "w", encoding="utf-8")
catalogo_albuns.write("")
catalogo_albuns.close()
def clicar_btn_registrar():
    global dados_album_juntos
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
    dados_album = nome_album + "  " + ano_lancamento + "  " + nome_banda + "  " + primeiro_album
    dados_album_juntos.append((nome_album, nome_banda, ano_lancamento, primeiro_album))
    catalogo_albuns.write(f'{dados_album} \n')
    catalogo_albuns.close()

# Função para exibir o conteúdo do bloco de notas gerado na janela de registro
def clicar_btn_mostrar():
    show = Toplevel()
    show.title("Music STORE, SHOW & SEARCH - Exibição")
    show.geometry("825x227")
    colunas = ("album", "banda", "ano", "primeiro")
    arvore = ttk.Treeview(show, columns=colunas, show='headings')
    arvore.heading('album', text='Álbum')
    arvore.heading('banda', text='Banda/artista')
    arvore.heading('ano', text='Ano de lançamento')
    arvore.heading('primeiro', text='É o primeiro álbum?')
    arvore.pack()
    catalogo_albuns = open("catalogo_albuns.txt", "r", encoding="utf-8")
    dados_albuns_txt = catalogo_albuns.readlines()
    for dados_album in dados_albuns_txt:
        dados_album = dados_album.split('  ')
        arvore.insert('', tkinter.END, values=dados_album) 
    arvore.grid(row=0, column=0, sticky='ns')
    barra_rolagem = ttk.Scrollbar(show, orient=tkinter.VERTICAL, command=arvore.yview)
    arvore.configure(yscroll=barra_rolagem.set)
    barra_rolagem.grid(row=0, column=1, sticky='ns')
    show.mainloop()

# Função que define os eventos que devem ocorrer quando o botão do critério de busca é clicado
def clicar_btn_criterio():
    global criterio_busca, lbl_criterio, cmbbox_criterio, txtbox_termo_busca, cmbbox_ano_interesse, txtbox_ano_interesse
    criterio_busca = cmbbox_criterio.get()
    lista_widgets_busca = []
    for widget in search.winfo_children():
        lista_widgets_busca.append(widget)
    for widget in lista_widgets_busca[3:]:
        widget.destroy()
    if criterio_busca == "Nome da banda/artista":
        Label(search, text="Termo de busca: ").place(x=50, y=200)
        txtbox_termo_busca = Entry(search, text="")
        txtbox_termo_busca.place(x=160, y=200)
    elif (criterio_busca == "Ano de lançamento"):
        Label(search, text="Ano de interesse: ").place(x=50, y=200)
        cmbbox_ano_interesse = ttk.Combobox(search, values=("inferior ou igual a", "igual a", "igual ou superior a"))
        cmbbox_ano_interesse.place(x=160, y=200)
        txtbox_ano_interesse = Entry(search, text="")
        txtbox_ano_interesse.place(x=320, y=200)
    btn_mostrar_selecionados = Button(search, text="SHOW", command=clicar_btn_mostrar_selecionados)
    btn_mostrar_selecionados.place(x=220, y=250)

# Função para abrir a janela de busca e captar os dados de interesse
def clicar_btn_buscar():
    global search, cmbbox_criterio
    search = Toplevel()
    search.title("Music STORE, SHOW & SEARCH - Busca")
    search.geometry("500x350")
    lbl_criterio = Label(search, text="Critério de busca: ")
    lbl_criterio.place(x=50, y=150)
    cmbbox_criterio = ttk.Combobox(search, values=("Nome da banda/artista", "Ano de lançamento"))
    cmbbox_criterio.place(x=160, y=150)
    btn_criterio = Button(search, text=">>>", command=clicar_btn_criterio)
    btn_criterio.place(x=310, y=145)
    search.mainloop()

# Função para exibir o conteúdo da lista de dados selecionados na janela de busca
def clicar_btn_mostrar_selecionados():
    dados_album_juntos_selecionados = []
    global dados_album_juntos, aux_dados
    if criterio_busca == "Nome da banda/artista":
        termo_busca = txtbox_termo_busca.get()
        for i in range(len(dados_album_juntos)):
            if termo_busca.lower() in dados_album_juntos[i][1].lower():
                dados_album_juntos_selecionados.append(dados_album_juntos[i])
    else:
        especificacao_ano = cmbbox_ano_interesse.get()
        ano_interesse = txtbox_ano_interesse.get()
        for j in range(len(dados_album_juntos)):
            if especificacao_ano == "inferior ou igual a":
                if dados_album_juntos[j][2] <= ano_interesse:
                    dados_album_juntos_selecionados.append(dados_album_juntos[j])
            elif especificacao_ano == "igual a": 
                if dados_album_juntos[j][2] == ano_interesse:
                    dados_album_juntos_selecionados.append(dados_album_juntos[j])
            elif especificacao_ano == "igual ou superior a":
                if dados_album_juntos[j][2] >= ano_interesse:
                    dados_album_juntos_selecionados.append(dados_album_juntos[j])
    show_selected = Toplevel()
    show_selected.title("Music STORE, SHOW & SEARCH - Exibição dos selecionados")
    show_selected.geometry("825x227")
    colunas_selecionados = ("album", "banda", "ano", "primeiro")
    arvore_selecionados = ttk.Treeview(show_selected, columns=colunas_selecionados, show='headings')
    arvore_selecionados.heading('album', text='Álbum')
    arvore_selecionados.heading('banda', text='Banda/artista')
    arvore_selecionados.heading('ano', text='Ano de lançamento')
    arvore_selecionados.heading('primeiro', text='É o primeiro álbum?')
    arvore_selecionados.pack()
    for dados_album in dados_album_juntos_selecionados:
        arvore_selecionados.insert('', tkinter.END, values=dados_album)
    arvore_selecionados.grid(row=0, column=0, sticky='ns')
    barra_rolagem_selecionados = ttk.Scrollbar(show_selected, orient=tkinter.VERTICAL, command=arvore_selecionados.yview)
    arvore_selecionados.configure(yscroll=barra_rolagem_selecionados.set)
    barra_rolagem_selecionados.grid(row=0, column=1, sticky='ns')
    show_selected.mainloop()
    
# Criação da janela principal
window = Tk()
window.title("Music STORE, SHOW & SEARCH - Registro")
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
btn_registrar.place(x=140, y=350)

# Botão para mostrar
btn_mostrar = Button(window, text="SHOW", command=clicar_btn_mostrar)
btn_mostrar.place(x=200, y=350)

# Botão para buscar
btn_buscar = Button(window, text="SEARCH", command=clicar_btn_buscar)
btn_buscar.place(x=260, y=350)

# Finalização da janela
window.mainloop()
