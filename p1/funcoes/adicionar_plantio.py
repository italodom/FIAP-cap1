from p1.funcoes.calculos.calcular_area_circulo import calcular_area_circulo
from p1.funcoes.calculos.calcular_area_retangulo import calcular_area_retangulo
from p1.funcoes.calculos.calcular_insumos import calcular_insumos
from p1.funcoes.database.database import banco_de_dados_culturas


def adicionar_plantio():
    print("Tipo de cultura disponivel:\n")
    print("1. Café (Área circula)")
    print("2. Soja (Área retangular)\n")

    tipo = input("Escolha o tipo de cultura: \n")
    print("\n")

    if tipo == "1":
        cultura = "Café"
        radio = float(input("Digite o radio (em metros): \n"))
        print("\n")
        area = calcular_area_circulo(radio)

        print(f"A área é: {area:.2f}")
        print("\n")
        insumos = calcular_insumos(cultura, area)
        banco_de_dados_culturas.append({
            "cultura": cultura,
            "area": area,
            "insumos": insumos,
        })

    elif tipo == "2":
        cultura = "Soja"
        largura = float(input("Digite a largura (em metros): "))
        comprimento = float(input("Digite o comprimento (em metros): \n"))
        print("\n")
        area = calcular_area_retangulo(largura, comprimento)

        print(f"A área é: {area:.2f}")
        print("\n")
        insumos = calcular_insumos(cultura, area)
        banco_de_dados_culturas.append({
            "cultura": cultura,
            "area": area,
            "insumos": insumos,
        })
    else:
        print("Opção inválida! Tente novamente. \n")
        return

    print("\nInsumos salvo com sucesso! \n")