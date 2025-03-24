import json
import os

def salvar_database(dados):
    caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.json")
    
    with open(caminho_arquivo, "w") as arquivo:
        json.dump(dados, arquivo, indent=2) 