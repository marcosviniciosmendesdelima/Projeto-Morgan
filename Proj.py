import json
import os

dados_iniciais = [
    {"nome": "Evidências", "artista": "Chitãozinho & Xororó", "gênero": "Sertanejo", "duração": "4:30"},
    {"nome": "Tempo Perdido", "artista": "Legião Urbana", "gênero": "Rock", "duração": "4:45"},
    {"nome": "Asa Branca", "artista": "Luiz Gonzaga", "gênero": "Forró", "duração": "3:20"},
    {"nome": "Lanterna dos Afogados", "artista": "Paralamas do Sucesso", "gênero": "Rock", "duração": "3:55"},
    {"nome": "Tocando em Frente", "artista": "Almir Sater", "gênero": "Música Popular Brasileira", "duração": "4:50"},
    {"nome": "Metade de Mim", "artista": "Oswaldo Montenegro", "gênero": "MPB", "duração": "3:40"},
    {"nome": "O Segundo Sol", "artista": "Cássia Eller", "gênero": "Rock", "duração": "4:25"},
    {"nome": "Romaria", "artista": "Renato Teixeira", "gênero": "Sertanejo", "duração": "3:35"},
    {"nome": "Pais e Filhos", "artista": "Legião Urbana", "gênero": "Rock", "duração": "5:05"},
    {"nome": "Andar com Fé", "artista": "Gilberto Gil", "gênero": "MPB", "duração": "3:15"},
    {"nome": "Céu Azul", "artista": "Charlie Brown Jr.", "gênero": "Rock", "duração": "3:32"}
]

def carregar_dados():
    if os.path.exists("musicas.json"):
        try:
            with open("musicas.json", "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            return []
    else:
        salvar_dados(dados_iniciais)
        return dados_iniciais

def salvar_dados(musicas):
    with open("musicas.json", "w", encoding="utf-8") as arquivo:
        json.dump(musicas, arquivo, indent=4, ensure_ascii=False)

def menu():
    print("\n=== MENU ===")
    print("[1] Adicionar música")
    print("[2] Listar músicas")
    print("[3] Buscar música")
    print("[4] Sair")

def adicionar_musica():
    nome = input("Nome da música: ")
    artista = input("Artista: ")
    genero = input("Gênero: ")
    duracao = input("Duração (ex: 3:45): ")

    nova_musica = {
        "nome": nome,
        "artista": artista,
        "gênero": genero,
        "duração": duracao
    }

    musicas.append(nova_musica)
    salvar_dados(musicas)
    print("Música adicionada com sucesso!")

def listar_musicas():
    if not musicas:
        print("Nenhuma música cadastrada.")
    else:
        print("\n=== Lista de Músicas ===")
        for i, m in enumerate(musicas, start=1):
            print(f"{i}. {m['nome']} - {m['artista']} ({m['gênero']}, {m['duração']})")

def buscar_musicas():
    print("\n=== Buscar Músicas ===")
    print("[1] Por artista")
    print("[2] Por gênero")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        termo = input("Digite o nome do artista: ").lower()
        resultados = [m for m in musicas if termo in m['artista'].lower()]
    elif escolha == "2":
        termo = input("Digite o gênero musical: ").lower()
        resultados = [m for m in musicas if termo in m['gênero'].lower()]
    else:
        print("Opção inválida.")
        return

    if resultados:
        print("\n=== Resultados da Busca ===")
        for i, m in enumerate(resultados, start=1):
            print(f"{i}. {m['nome']} - {m['artista']} ({m['gênero']}, {m['duração']})")
    else:
        print("Nenhuma música encontrada com esse critério.")

musicas = carregar_dados()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_musica()
    elif opcao == "2":
        listar_musicas()
    elif opcao == "3":
        buscar_musicas()
    elif opcao == "4":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
