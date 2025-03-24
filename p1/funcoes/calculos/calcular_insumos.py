from p1.config import insumos_por_cultura
from p1.funcoes.calculos.formatar_numero import formatar_numero_br
from p1.funcoes.calculos.extrair_unidade_medida import extrair_unidade_medida   

def calcular_insumos(cultura, area):
    hectares = area / 10000

    insumos = {}
    for insumo, qtd_insumo in insumos_por_cultura[cultura].items():
        total_insumo = hectares * qtd_insumo
        insumos[insumo] = total_insumo
        print(f"{extrair_unidade_medida(insumo)[0]} ({extrair_unidade_medida(insumo)[1]}): {formatar_numero_br(total_insumo)}")

    return insumos