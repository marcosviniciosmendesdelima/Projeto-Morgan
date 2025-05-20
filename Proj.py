import json
#TESTE 12:14
def carregar_dados():
    try:
        with open("musicas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados():
    with open("musicas.json", "w", encoding="utf-8") as arquivo:
        json.dump(musicas, arquivo, ensure_ascii=False, indent=4)

musicas = carregar_dados() # Carrega as músicas do arquivo JSON (fora da função)

def menu():
    print("\n--- MENU ---")
    print("[1] Adicionar música")
    print("[2] Listar músicas")
    print("[3] Buscar música")
    print("[4] Sair")

def adicionar_musica():
    nome = input("Nome da música: ")
    artista = input("Artista: ")
    genero = input("Gênero: ")
    duracao = input("Duração (ex: 4:30): ")

    musica = {
        "nome": nome,
        "artista": artista,
        "gênero": genero,
        "duração": duracao
    }

    musicas.append(musica)
    salvar_dados()
    print("Música adicionada com sucesso!")

def listar_musicas():
    if not musicas:
        print("Nenhuma música cadastrada.")
    else:
        print("\n--- Lista de Músicas ---")
        for idx, musica in enumerate(musicas, start=1):
            print(f"{idx}. {musica['nome']} - {musica['artista']} | {musica['gênero']} | {musica['duração']}")

def buscar_musicas():
    print("\nBuscar por:")
    print("[1] Artista")
    print("[2] Gênero")
    escolha = input("Escolha uma opção: ")

    termo = input("Digite o termo de busca: ").lower()
    resultados = []

    for musica in musicas:
        if escolha == "1" and termo in musica["artista"].lower():
            resultados.append(musica)
        elif escolha == "2" and termo in musica["gênero"].lower():
            resultados.append(musica)

    if not resultados:
        print("Nenhuma música encontrada com esse critério.")
    else:
        print("\n--- Resultados da Busca ---")
        for idx, musica in enumerate(resultados, start=1):
            print(f"{idx}. {musica['nome']} - {musica['artista']} | {musica['gênero']} | {musica['duração']}")

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
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
