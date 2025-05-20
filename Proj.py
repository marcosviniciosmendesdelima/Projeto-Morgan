import json


def carregar_dados():
    try:
        with open("musicas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(musicas):
    with open("musicas.json", "w", encoding="utf-8") as arquivo:
        json.dump(musicas, arquivo, indent=4, ensure_ascii=False)

musicas = carregar_dados()

def menu():
    print("\n=== MENU ===")
    print("[1] Adicionar música")
    print("[2] Listar músicas")
    print("[3] Sair")
    print("[4] Buscar música")

def adicionar_musica():
    nome = input("Nome da música: ")
    artista = input("Artista: ")
    genero = input("Gênero: ")
    duracao = input("Duração (ex: 3:45): ")

    musica = {
        "nome": nome,
        "artista": artista,
        "genero": genero,
        "duracao": duracao
    }

    musicas.append(musica)
    salvar_dados(musicas)
    print("Música adicionada com sucesso!")

def listar_musicas():
    if not musicas:
        print("Nenhuma música cadastrada.")
    else:
        print("\n=== Lista de Músicas ===")
        for i, m in enumerate(musicas, 1):
            print(f"{i}. {m['nome']} - {m['artista']} ({m['genero']}, {m['duracao']})")

def buscar_musicas():
    print("\n=== Buscar Música ===")
    print("[1] Buscar por Artista")
    print("[2] Buscar por Gênero")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        campo = "artista"
    elif opcao == "2":
        campo = "genero"
    else:
        print("Opção inválida.")
        return

    termo = input(f"Digite o {campo} para buscar: ").lower()
    resultados = []

    for m in musicas:
        if termo in m[campo].lower():
            resultados.append(m)

    if not resultados:
        print("Nenhuma música encontrada.")
    else:
        print(f"\n=== Resultados da Busca por {campo} ===")
        for i, m in enumerate(resultados, 1):
            print(f"{i}. {m['nome']} - {m['artista']} ({m['genero']}, {m['duracao']})")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_musica()
    elif escolha == "2":
        listar_musicas()
    elif escolha == "3":
        print("Saindo do programa. Até logo!")
        break
    elif escolha == "4":
        buscar_musicas()
    else:
        print("Opção inválida. Tente novamente.")
