from p1.funcoes.calculos.calcular_area_circulo import calcular_area_circulo
from p1.funcoes.calculos.calcular_area_retangulo import calcular_area_retangulo
from p1.funcoes.calculos.calcular_insumos import calcular_insumos
from p1.funcoes.database.salvar_database import salvar_database
from p1.funcoes.database.database import banco_de_dados_culturas


def atualizar_cultura():
    index = 1
    for dado in banco_de_dados_culturas:
        print("\n======================================")
        print(f"Id: {index}")
        print(f"Cultura: {dado['cultura']}")
        print(f"Área: {dado['area']}")
        index += 1

    id = int(input("\nDigite o ID da cultura que deseja atualizar:"))
    cultura_selecionada = banco_de_dados_culturas[id - 1]

    if cultura_selecionada["cultura"] == "Café":
        cultura = "Café"
        radio = float(input("Digite o radio (em metros): \n"))
        print("\n")
        area = calcular_area_circulo(radio)

        print(f"A área é: {area:.2f}")
        print("\n")
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
        print("\n")
        area = calcular_area_retangulo(largura, comprimento)

        print(f"A área é: {area:.2f}")
        print("\n")
        insumos = calcular_insumos(cultura, area)
        banco_de_dados_culturas[id - 1] = {
            "cultura": cultura,
            "area": area,
            "insumos": insumos,
        }
        salvar_database(banco_de_dados_culturas)

    print("\nInsumos salvo com sucesso! \n")