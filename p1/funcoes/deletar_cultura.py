from p1.funcoes.database.database import banco_de_dados_culturas
from p1.funcoes.database.salvar_database import salvar_database


def deletar_cultura():
    index = 1
    for dado in banco_de_dados_culturas:
        print("\n======================================")
        print(f"Id: {index}")
        print(f"Cultura: {dado['cultura']}")
        print(f"Área: {dado['area']}")
        index += 1

    id = int(input("\nDigite o ID da cultura que deseja deletar:"))
    cultura_selecionada = id - 1
    banco_de_dados_culturas.pop(cultura_selecionada)
    salvar_database(banco_de_dados_culturas)
    print("\nCultura removida com sucesso! \n")