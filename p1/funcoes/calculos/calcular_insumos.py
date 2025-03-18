from p1.config import insumos_por_cultura


def calcular_insumos(cultura, area):
    hectares = area / 10000

    insumos = {}
    for insumo, qtd_insumo in insumos_por_cultura[cultura].items():
        total_insumo = hectares * qtd_insumo
        insumos[insumo] = total_insumo
        print(f"{insumo}: {total_insumo:.2f}")

    return insumos