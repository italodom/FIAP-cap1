from p1.funcoes.calculos.calcular_area_circulo import calcular_area_circulo
from p1.funcoes.calculos.calcular_area_retangulo import calcular_area_retangulo
from p1.funcoes.calculos.calcular_insumos import calcular_insumos
from p1.funcoes.calculos.converte_para_hectares import converter_para_hectares
from p1.funcoes.calculos.formatar_numero import formatar_numero_br
from p1.funcoes.database.database import banco_de_dados_culturas
from p1.funcoes.database.salvar_database import salvar_database


def adicionar_plantio():
    print("Tipo de cultura disponivel:\n")
    print("1. Café (Área circula)")
    print("2. Soja (Área retangular)\n")

    tipo = input("Escolha o tipo de cultura: \n")

    if tipo == "1":
        cultura = "Café"
        radio = float(input("Digite o radio (em metros): \n"))
        area = calcular_area_circulo(radio)
        hectares = converter_para_hectares(area)

        print(f"\nA cultura é: {cultura}")
        print(f"A área é de: {formatar_numero_br(area)} m² (~ {formatar_numero_br(hectares)} hectares)\n")
        insumos = calcular_insumos(cultura, area)
        banco_de_dados_culturas.append({
            "cultura": cultura,
            "area": area,
            "insumos": insumos,
        })
        salvar_database(banco_de_dados_culturas)

    elif tipo == "2":
        cultura = "Soja"
        largura = float(input("Digite a largura (em metros): "))
        comprimento = float(input("Digite o comprimento (em metros):"))
        area = calcular_area_retangulo(largura, comprimento)
        hectares = converter_para_hectares(area)

        print(f"\nA cultura é: {cultura}")
        print(f"\nA área é de: {formatar_numero_br(area)} m² (~ {formatar_numero_br(hectares)} hectares)\n")
        insumos = calcular_insumos(cultura, area)
        banco_de_dados_culturas.append({
            "cultura": cultura,
            "area": area,
            "insumos": insumos,
        })
        salvar_database(banco_de_dados_culturas)
    else:
        print("Opção inválida! Tente novamente. \n")
        return

    print("\nInsumos salvo com sucesso! \n")