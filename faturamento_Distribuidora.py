import json

with open("dados.json", encoding='utf-8') as faturamento_diario_distribuidora:
    dados = json.load(faturamento_diario_distribuidora)

dias_uteis = [(dado["dia"], dado["valor"]) for dado in dados if dado["valor"] != 0.0]

if dias_uteis:
    
    menor_dia, menor_valor = min(dias_uteis, key=lambda x: x[1])
    maior_dia, maior_valor = max(dias_uteis, key=lambda x: x[1])

    total_faturamento = sum(valor for dia, valor in dias_uteis)
    media = total_faturamento / len(dias_uteis)

    dias_superior_media = sum(1 for dia, valor in dias_uteis if valor > media)

    print(f"O menor faturamento ocorreu no dia {menor_dia}, valor de faturamento R${menor_valor}")
    print(f"O maior faturamento ocorreu no dia {maior_dia}, valor de faturamento R${maior_valor}")
    print(f"{dias_superior_media} dias no mês superaram a média mensal de R${round(media, 2)}")
else:
    print("Não há dados de faturamento disponíveis.")
