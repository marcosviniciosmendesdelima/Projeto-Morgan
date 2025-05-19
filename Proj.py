# Armazenar músicas

musicas = []

# Criar uma função Menu

def menu():
    
    print("\--- MENU ---")
    print("[1] Adicionar música")
    print("[2] Listar músicas")
    print("[3] Sair")
    
# Função para adicionar uma música 

def adicionar_msica ():
    
    nome = input("Nome da música:")
    artista = input("Artista:")
    genero = input("Genero:")
    duracao = input("Duração (ex: 4:30):")
    
    musica = {
        
        "nome": nome, 
        "artista": artista,
        "gênero": genero,
        "duração": duracao
        
    }
    
    musicas.append(musicas)
    
    print("Música adicionada com sucesso!")
    
# Função para listas todas as músicas

def listar_musicas():
    
    if not musicas:
        
        print("Nenhuma música cadastrada.")
        
    else: 
        
        print("n\-- Lista de Músicas --")
        
        for idx, musica in enumerate(musicas, start=1):
            
            print(f"{idx}.{musica['nome']} - {musica['artista']})|{musica['gênero']}|{musica['duração']}")
            
# Loop Principal

while True:

  menu()
  opcao = input("Escolha uma opção:")
  
if opçao == "1":
     adcionar_musica()
     
elif opcao == "2":
     listar_musicas()
     
elif opcao == "3":
     print("Saindo do programa. Até mais!")
 
else:
    
     print("Opção inválida. Tente novamente.")