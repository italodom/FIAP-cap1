from p1.funcoes.calculos.calcular_area_retangulo import calcular_area_retangulo
from p1.funcoes.calculos.converte_para_hectares import converter_para_hectares
from p1.funcoes.database.database import banco_de_dados_culturas
from p1.funcoes.calculos.formatar_numero import formatar_numero_br

def listar_culturas():
    try:
        if (len(banco_de_dados_culturas) <= 0):
            print("\nNenhuma cultura cadastrada! \n")
            return

        index = 1
        for dado in banco_de_dados_culturas:
            area = dado['area']
            hectares = converter_para_hectares(area)

            print("\n======================================")
            print(f"Id: {index}")
            print(f"Cultura: {dado['cultura']}")
            print(f"A área é de: {formatar_numero_br(area)} m² (~ {formatar_numero_br(hectares)} hectares)\n")

            print(f"Insumos:\n")
            for insumo, qtd_insumo in dado['insumos'].items():
                print(f"{insumo}: {formatar_numero_br(qtd_insumo)}")
            index += 1
    except Exception as e:
        print(f"\nErro ao listar culturas: {e}\n")