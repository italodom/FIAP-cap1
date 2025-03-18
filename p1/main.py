import json

banco_de_dados_culturas = []

insumos_por_cultura = {
    "Café": {
        "Nitrogênio (kg/ha)": 100,
        "Fósforo (kg/ha)": 50,
        "Potássio (kg/ha)": 60,
        "Micronutrientes (Boro, Zinco) (kg/ha)": 5,
        "Calcário (t/ha)": 3,
        "Gesso Agrícola (t/ha)": 1.5,
        "Inseticidas (mL/ha)": 1500,
        "Fungicidas (mL/ha)": 2000,
        "Herbicidas (L/ha)": 2
    },
    "Soja": {
        "Fósforo (kg/ha)": 40,
        "Potássio (kg/ha)": 50,
        "Micronutrientes e Enxofre (S) (kg/ha)": 10,
        "Bradyrhizobium (com Mo e Co) (mL/ha)": 500,
        "Calcário (t/ha)": 2.5,
        "Gesso Agrícola (t/ha)": 1,
        "Fungicidas (mL/ha)": 2500,
        "Inseticidas (mL/ha)": 1800,
        "Aplicações Foliares de Micronutrientes (mL/ha)": 300
    }
}

def menu():
    while True:
        print("\nFarmTech Solutions - Agricultura Digital")
        print("1. Adicionar Cultura")
        print("2. Listar Culturas e Insumos")
        print("3. Atualizar Cultura")
        print("4. Remover Cultura")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_plantio()
        elif opcao == "2":
            listar_culturas()
        elif opcao == "3":
            atualizar_cultura()
        elif opcao == "4":
            deletar_cultura()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

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
        # banco_de_dados_culturas.append({
        #     "cultura": cultura,
        #     "area": area,
        #     "insumos": insumos,
        # })

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

def listar_culturas():
    ler_database()

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

    print("\nInsumos salvo com sucesso! \n")

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

def calcular_area_circulo(radio):
    pi = 3.141592653589793
    return pi * (radio ** 2)

def calcular_area_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_insumos(cultura, area):
    hectares = area / 10000

    insumos = {}
    for insumo, qtd_insumo in insumos_por_cultura[cultura].items():
        total_insumo = hectares * qtd_insumo
        insumos[insumo] = total_insumo
        print(f"{insumo}: {total_insumo:.2f}")

    return insumos

def ler_database():
    with open("database.json", "r") as arquivo:
        dados = json.load(arquivo)
        banco_de_dados_culturas = dados


menu()

