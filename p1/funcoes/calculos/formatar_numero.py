def formatar_numero_br(numero, casas=2):

    texto = f"{numero:.{casas}f}"

    partes = texto.split('.')
    parte_inteira = partes[0]
    parte_decimal = partes[1] if len(partes) > 1 else ""
    
    if len(parte_inteira) > 3:
        parte_inteira = '.'.join([parte_inteira[:-3], parte_inteira[-3:]])
    
    return f"{parte_inteira},{parte_decimal}"