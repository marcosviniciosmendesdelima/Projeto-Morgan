# ---------------------------------------------
# PROJETO: Interface gráfica para o catálogo de músicas
# ETAPA 4: Exibir músicas cadastradas com Tkinter
# ---------------------------------------------

# 1. Importar as bibliotecas necessárias
# - tkinter: para criar a interface gráfica
# - messagebox: para exibir mensagens (caso precise)
# - json: para carregar os dados salvos no arquivo
import tkinter as tk
from tkinter import messagebox
import json

# 2. Função para carregar os dados do arquivo JSON
# - Caso o arquivo não exista ou esteja corrompido, retorna uma lista vazia
def carregar_dados():
    try:
        with open("musicas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# 3. Carregamos a lista de músicas na variável global
musicas = carregar_dados()

# 4. Criamos uma função para mostrar as músicas em uma lista gráfica (Listbox)
# - Primeiro limpamos a lista
# - Depois adicionamos cada música formatada
def listar_musicas_tk():
    lista.delete(0, tk.END)
    if not musicas:
        lista.insert(tk.END, "Nenhuma música cadastrada.")
    else:
        for m in musicas:
            texto = f"{m['nome']} - {m['artista']} | {m['gênero']} | {m['duração']}"
            lista.insert(tk.END, texto)

# 5. Criamos a janela principal da aplicação
# - Definimos um título e um tamanho
janela = tk.Tk()
janela.title("Catálogo de Músicas")
janela.geometry("600x400")

# 6. Adicionamos um título de texto no topo da janela
titulo = tk.Label(janela, text="Minhas Músicas", font=("Arial", 16))
titulo.pack(pady=10)

# 7. Criamos um Listbox (lista gráfica) para exibir as músicas
# - Definimos o tamanho da área
lista = tk.Listbox(janela, width=80, height=15)
lista.pack()

# 8. Adicionamos um botão que chama a função de atualizar a lista
btn_atualizar = tk.Button(janela, text="Atualizar Lista", command=listar_musicas_tk)
btn_atualizar.pack(pady=10)

# 9. Chamamos a função uma vez ao iniciar a interface
# - Isso faz com que a lista apareça já preenchida
listar_musicas_tk()

# 10. Mantemos a janela aberta com o loop principal do Tkinter
janela.mainloop()
