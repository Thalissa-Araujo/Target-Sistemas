valores_por_estado = {
'SP': 67836.43, 
'RJ': 36678.66, 
'MG': 29229.88, 
'ES': 27165.48, 
'Outros': 19849.53}

def calcular_percentuais(valores): 
    valor_total_mensal = sum(valores.values()) 
    percentuais = {estado: round((valor / valor_total_mensal) * 100, 2) 
    
    for estado, valor in valores.items()} 
    
    for estado, percentual in percentuais.items(): 
        print(f"O percentual de {estado} é de {percentual}%")

calcular_percentuais(valores_por_estado)