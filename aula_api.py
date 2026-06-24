#%%

import requests #realizar requisições HTTP
import json #trabalhar com arquivos JSON
from tqdm import tqdm #barra de progresso
import pandas as pd #manipulação de dados

# Lista de CEPs válidos para consulta
ceps_validos = [
    "01001-000", # São Paulo - SP (Sé)
    "20040-003", # Rio de Janeiro - RJ (Centro)
    "70070-901", # Brasília - DF (Asa Norte)
    "30130-010", # Belo Horizonte - MG (Funcionários)
    "80020-030", # Curitiba - PR (Centro)
    "90010-150", # Porto Alegre - RS (Centro Histórico)
    "60060-150", # Fortaleza - CE (Centro)
    "40026-010", # Salvador - BA (Comércio)
    "50030-230", # Recife - PE (Recife)
    "78005-500", # Cuiabá - MT (Centro Norte)
    "69005-040", # Manaus - AM (Centro)
    "57020-590", # Maceió - AL (Centro)
    "79002-250", # Campo Grande - MS (Centro)
    "88015-420", # Florianópolis - SC (Centro)
    "39400-004", # Montes Claros - MG (Centro)
    "13010-001", # Campinas - SP (Centro)
    "29015-100", # Vitória - ES (Centro)
    "58013-600", # João Pessoa - PB (Varadouro)
    "77001-002", # Palmas - TO (Plano Diretor Sul)
    "84010-020"  # Ponta Grossa - PR (Centro)
]


# Fazer requisição para um CEP específico
url = "https://viacep.com.br/ws/84051060/json/"


# Fazer requisições para todos os CEPs válidos e armazenar os dados em uma lista
dados = []


for cep in tqdm(ceps_validos):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    dados.append(response.json())


dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", index=False, encoding="utf-8-sig")


# Salvar os dados em um arquivo JSON
with open("ceps.json", "w", encoding="utf-8") as file:
    
    if response.status_code == 200:
        print("Requisição bem-sucedida! Dados salvos em 'ceps.json'")
        json.dump(dados, file, indent=4, ensure_ascii=False)





