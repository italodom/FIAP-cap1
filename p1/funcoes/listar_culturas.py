from p1.funcoes.database.database import banco_de_dados_culturas
from p1.funcoes.calculos.formatar_numero import formatar_numero_br

def listar_culturas():
    try:
        if (len(banco_de_dados_culturas) <= 0):
            print("\nNenhuma cultura cadastrada! \n")
            return

        index = 1
        for dado in banco_de_dados_culturas:
            print("\n======================================")
            print(f"Id: {index}")
            print(f"Cultura: {dado['cultura']}")
            print(f"Área: {formatar_numero_br(dado['area'])} m²")
            print(f"Insumos:\n")
            for insumo, qtd_insumo in dado['insumos'].items():
                print(f"{insumo}: {formatar_numero_br(qtd_insumo)}")
            index += 1
    except Exception as e:
        print(f"\nErro ao listar culturas: {e}\n")