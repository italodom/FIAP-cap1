from p1.funcoes.database.database import banco_de_dados_culturas


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

    print("\nCultura removida com sucesso! \n")