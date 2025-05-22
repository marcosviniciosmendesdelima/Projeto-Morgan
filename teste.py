import json

def carregar_dados():
    try:
        with open("musicas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados():
    with open("musicas.json", "w", encoding="utf-8") as arquivo:
        json.dump(musicas, arquivo, ensure_ascii=False, indent=4)

musicas = carregar_dados() 

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

def editar_musica():
    if not musicas:
        print("Nenhuma música cadastrada.")
        return

    print("\n--- Editar Música ---")
    for idx, musica in enumerate(musicas, start=1):
        print(f"{idx}. {musica['nome']} - {musica['artista']}")

    try:
        escolha = int(input("Digite o número da música que deseja editar: "))
        if escolha < 1 or escolha > len(musicas):
            print("Número inválido.")
            return
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        return

    musica = musicas[escolha - 1]

    print("\nPressione Enter para manter o valor atual.")

    novo_nome = input(f"Nome atual: {musica['nome']} -> Novo nome: ")
    novo_artista = input(f"Artista atual: {musica['artista']} -> Novo artista: ")
    novo_genero = input(f"Gênero atual: {musica['gênero']} -> Novo gênero: ")
    nova_duracao = input(f"Duração atual: {musica['duração']} -> Nova duração: ")

    if novo_nome:
        musica['nome'] = novo_nome
    if novo_artista:
        musica['artista'] = novo_artista
    if novo_genero:
        musica['gênero'] = novo_genero
    if nova_duracao:
        musica['duração'] = nova_duracao

    salvar_dados()
    print("Música editada com sucesso!")

def remover_musica():
    if not musicas:
        print("Nenhuma música cadastrada.")
        return

    print("\n--- Remover Música ---")
    for idx, musica in enumerate(musicas, start=1):
        print(f"{idx}. {musica['nome']} - {musica['artista']}")

    try:
        escolha = int(input("Digite o número da música que deseja remover: "))
        if escolha < 1 or escolha > len(musicas):
            print("Número inválido.")
            return
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        return

    musica = musicas[escolha - 1]
    confirmacao = input(f"Tem certeza que deseja remover '{musica['nome']}' de {musica['artista']}? (S/N): ").strip().upper()

    if confirmacao == "S":
        del musicas[escolha - 1]
        salvar_dados()
        print("Música removida com sucesso!")
    else:
        print("Remoção cancelada.")

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
