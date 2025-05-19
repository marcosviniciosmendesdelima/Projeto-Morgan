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

def menu():
    print("\n--- MENU ---")
    print("[1] Adicionar música")
    print("[2] Listar músicas")
    print("[3] Sair")

def adicionar_musica():
    nome = input("Nome da música: ")
    artista = input("Artista: ")
    genero = input("Gênero: ")
    duracao = input("Duração (min:seg): ")

    musica = {
        "nome": nome,
        "artista": artista,
        "gênero": genero,
        "duração": duracao
    }

    musicas.append(musica)

    salvar_dados(musicas)

    print("Música adicionada com sucesso!")

def listar_musicas():
    if not musicas:
        print("Nenhuma música cadastrada.")
    else:
        print("\n--- Lista de Músicas ---")
        for i, musica in enumerate(musicas, start=1):
            print(f"{i}. {musica['nome']} - {musica['artista']} ({musica['gênero']}) [{musica['duração']}]")

musicas = carregar_dados()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_musica()
    elif opcao == "2":
        listar_musicas()
    elif opcao == "3":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
