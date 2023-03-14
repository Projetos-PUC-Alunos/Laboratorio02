import csv
import os

# Caminho do arquivo CSV
caminho_arquivo = 'arquivo.csv'

# Pasta onde o repositório será clonado
caminho_destino = 'pasta_destino'

# Abre o arquivo CSV
with open(caminho_arquivo, 'r') as csv_file:
    # Lê o arquivo CSV com um objeto reader
    csv_reader = csv.reader(csv_file)

    # Pula a primeira linha do arquivo CSV (cabeçalho)
    next(csv_reader)

    # Loop através de cada linha do arquivo CSV
    for linha in csv_reader:
        # Extrai a coluna "url" da linha atual
        url = linha[0]

        # Clona o repositório com base na URL usando o comando git clone
        os.system('git clone ' + url + ' ' + caminho_destino)
