import json


def ler_database():
    with open("database.json", "r") as arquivo:
        dados = json.load(arquivo)
        banco_de_dados_culturas = dados