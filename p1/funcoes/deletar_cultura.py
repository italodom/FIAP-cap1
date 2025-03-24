from p1.funcoes.calculos.converte_para_hectares import converter_para_hectares
from p1.funcoes.calculos.formatar_numero import formatar_numero_br
from p1.funcoes.database.database import banco_de_dados_culturas
from p1.funcoes.database.salvar_database import salvar_database


def deletar_cultura():
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
        index += 1

    id = int(input("\nDigite o ID da cultura que deseja deletar:"))

    if id <= 0 or id > len(banco_de_dados_culturas):
        print("\nCultura não encontrada! O ID informado não existe.\n")
        return

    cultura_selecionada = id - 1
    banco_de_dados_culturas.pop(cultura_selecionada)
    salvar_database(banco_de_dados_culturas)
    print("\nCultura removida com sucesso! \n")