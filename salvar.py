# Importar a biblioteca json para lidar com arquivos estruturados
import json

# Criar uma função chamada carregar_dados()
# - Tenta abrir o arquivo "musicas.json" em modo de leitura -> with open("musicas.json", "r", encoding="utf-8") as arquivo:
# - Se conseguir, usa json.load() para transformar o conteúdo em uma lista de dicionários
# - Se o arquivo não existir ou der erro, retorna uma lista vazia
# - Dica: usar try/except para tratar erros de arquivo

# Criar uma função chamada salvar_dados()
# - Abre (ou cria) o arquivo "musicas.json" em modo de escrita
# - Usa json.dump() para salvar a lista de músicas no arquivo
# - Usar indent=4 no json.dump() para deixar o arquivo legível

# Chamar carregar_dados() logo no início do programa e armazenar o retorno na variável musicas

# No final da função adicionar_musica(), depois de adicionar a música na lista,
# chamar salvar_dados() para garantir que a nova música será salva no arquivo

# Quando o programa for iniciado novamente, ele deve carregar as músicas do arquivo automaticamente