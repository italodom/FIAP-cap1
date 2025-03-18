import re

def extrair_unidade_medida(nome_insumo):
    
    padrao = r'\((.*?)\)'
    resultado = re.search(padrao, nome_insumo)
    
    if resultado:
        unidade_completa = resultado.group(1)
        unidade_basica = unidade_completa.split('/')[0]
        
       
        nome_limpo = nome_insumo.split(' (')[0].strip()
        
        return (nome_limpo, unidade_basica)
    else:
       
        return (nome_insumo, "")