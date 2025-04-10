import requests, os

"""
- Modo operante:

TODO: Pega link raw do .exe no repositório Github ou link setado no DB;
TODO: Pega nome fixo ou customizado do DB;
TODO: Salva no diretório fixo (AppData/Roaming ou Appdata/Local) ou pasta setada no DB;
TODO: Pega nome fixo ou custom do DB;

"""

# No momento, consegue baixar .exe de repositório github com link RAW;
url = "URL GITHUB RAW"

# TODO: Nome provisório de arquivo, pega nome do link do github (FICA FEIO SEM ACENTUAÇÕES);
# O idal seria setar um default no DB ou um nome custom;
nome_arquivo_github_raw = url.split("/")[-1]

# TODO: Caso caminho seja default;
caminho_appdata = os.getenv('APPDATA')  # AppData/Roaming;
if not caminho_appdata:
  caminho_appdata = os.getenv('LOCALAPPDATA')  # AppData/Local?;

# Junta local de download (AppData ou custom) e cria uma pasta com um nome (Default ou Custom);
nome_pasta = "NomeDaPasta"
caminho_pasta_download = os.path.join(caminho_appdata, nome_pasta)

# Verifica se pasta existe;
os.makedirs(caminho_pasta_download, exist_ok=True)

# Caminho de download (Local de download default ou custom + nome da pasta);
caminho_download = os.path.join(caminho_pasta_download, nome_arquivo_github_raw)

# Download do arquivo .exe de acordo com o DB;
resposta = requests.get(url)

# Verifica realização do download;
if resposta.status_code == 200:
  with open(caminho_download, "wb") as file:
    file.write(resposta.content)
  print(f"Arquivo baixado em: {caminho_download} como {nome_arquivo_github_raw}")
else:
  print(f"Falha no Download. Status code: {resposta.status_code}")