# Importar a biblioteca json para lidar com arquivos estruturados
import json

# Função para carregar os dados do arquivo "musicas.json"
def carregar_dados():
    try:
        # Tenta abrir o arquivo em modo leitura
        with open("musicas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)  # Transforma o conteúdo JSON em lista de dicionários
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Se o arquivo não existir ou estiver vazio/corrompido, retorna uma lista vazia

# Função para salvar os dados no arquivo "musicas.json"
def salvar_dados(musicas):
    # Abre (ou cria) o arquivo em modo escrita
    with open("musicas.json", "w", encoding="utf-8") as arquivo:
        # Salva a lista no arquivo com indentação para facilitar leitura
        json.dump(musicas, arquivo, indent=4, ensure_ascii=False)

# Função para mostrar o menu principal
def menu():
    print("\n--- MENU ---")
    print("[1] Adicionar música")
    print("[2] Listar músicas")
    print("[3] Sair")

# Função para adicionar uma música
def adicionar_musica():
    nome = input("Nome da música: ")
    artista = input("Artista: ")
    genero = input("Gênero: ")
    duracao = input("Duração (min:seg): ")

    # Cria um dicionário com os dados
    musica = {
        "nome": nome,
        "artista": artista,
        "gênero": genero,
        "duração": duracao
    }

    # Adiciona à lista de músicas
    musicas.append(musica)

    # Salva os dados no arquivo após adicionar
    salvar_dados(musicas)

    print("Música adicionada com sucesso!")

# Função para listar todas as músicas
def listar_musicas():
    if not musicas:
        print("Nenhuma música cadastrada.")
    else:
        print("\n--- Lista de Músicas ---")
        for i, musica in enumerate(musicas, start=1):
            print(f"{i}. {musica['nome']} - {musica['artista']} ({musica['gênero']}) [{musica['duração']}]")

# ===== Programa principal =====

# Carrega as músicas do arquivo ao iniciar
musicas = carregar_dados()

# Laço principal do menu
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
