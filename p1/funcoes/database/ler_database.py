import json
import os


def ler_database():
    caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.json")
    
    try:
        with open(caminho_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        
        return []