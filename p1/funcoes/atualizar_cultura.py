from p1.funcoes.calculos.calcular_area_circulo import calcular_area_circulo
from p1.funcoes.calculos.calcular_area_retangulo import calcular_area_retangulo
from p1.funcoes.calculos.calcular_insumos import calcular_insumos
from p1.funcoes.calculos.converte_para_hectares import converter_para_hectares
from p1.funcoes.calculos.formatar_numero import formatar_numero_br
from p1.funcoes.database.salvar_database import salvar_database
from p1.funcoes.database.database import banco_de_dados_culturas


def atualizar_cultura():
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

    id = int(input("\nDigite o ID da cultura que deseja atualizar:"))

    if id <= 0 or id > len(banco_de_dados_culturas):
        print("\nCultura não encontrada! O ID informado não existe.\n")
        return

    cultura_selecionada = banco_de_dados_culturas[id - 1]

    if cultura_selecionada["cultura"] == "Café":
        cultura = "Café"
        radio = float(input("Digite o radio (em metros):"))
        area = calcular_area_circulo(radio)
        hectares = converter_para_hectares(area)

        print(f"\nA cultura é: {cultura}")
        print(f"A área é de: {formatar_numero_br(area)} m² (~ {formatar_numero_br(hectares)} hectares)\n")
        insumos = calcular_insumos(cultura, area)
        banco_de_dados_culturas[id - 1] = {
            "cultura": cultura,
            "area": area,
            "insumos": insumos,
        }
    elif cultura_selecionada["cultura"] == "Soja":
        cultura = "Soja"
        largura = float(input("Digite a largura (em metros): "))
        comprimento = float(input("Digite o comprimento (em metros): \n"))
        area = calcular_area_retangulo(largura, comprimento)
        hectares = converter_para_hectares(area)

        print(f"\nA cultura é: {cultura}")
        print(f"A área é de: {formatar_numero_br(area)} m² (~ {formatar_numero_br(hectares)} hectares)\n")
        insumos = calcular_insumos(cultura, area)
        banco_de_dados_culturas[id - 1] = {
            "cultura": cultura,
            "area": area,
            "insumos": insumos,
        }
        salvar_database(banco_de_dados_culturas)

    print("\nInsumos salvo com sucesso! \n")