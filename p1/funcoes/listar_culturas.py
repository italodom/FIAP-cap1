from p1.funcoes.database.database import banco_de_dados_culturas


def listar_culturas():

    if (len(banco_de_dados_culturas) <= 0):
        print("\nNenhum cultura cadastrada! \n")
        return

    index = 1
    for dado in banco_de_dados_culturas:
        print("\n======================================")
        print(f"Id: {index}")
        print(f"Cultura: {dado['cultura']}")
        print(f"Área: {dado['area']}")
        print(f"Insumos:\n")
        for insumo, qtd_insumo in dado['insumos'].items():
            print(f"{insumo}: {qtd_insumo:.2f}")
        index += 1