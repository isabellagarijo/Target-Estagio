import json

faturamentos_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Função para processar os dados de faturamento
def processar_faturamento(caminho_arquivo):
    with open(caminho_arquivo, 'r') as json_file:
        dados = json.load(json_file)

    # Extrair os valores de faturamento
    faturamentos = [item['valor'] for item in dados]
    
    # Filtrar dias válidos (com faturamento > 0)
    dias_validos = [valor for valor in faturamentos if valor > 0]

    # Menor valor de faturamento
    menor_faturamento = min(faturamentos)

    # Menor valor de faturamento em dias válidos
    menor_faturamento_validos = min(dias_validos) if dias_validos else 0

    # Maior valor de faturamento
    maior_faturamento = max(faturamentos)

    # Média mensal (considerando apenas dias com faturamento > 0)
    #dias_validos = [valor for valor in faturamentos if valor > 0]
    media_faturamento = sum(dias_validos) / len(dias_validos) if dias_validos else 0

    # Número de dias com faturamento acima da média
    dias_acima_media = sum(1 for faturamento in faturamentos if faturamento > media_faturamento)

    faturamento_total = sum(dias_validos)



    return menor_faturamento, menor_faturamento_validos, maior_faturamento, dias_acima_media,faturamento_total

# Caminho do arquivo JSON
caminho_arquivo = 'C:\\Users\\Isabella\\Downloads\\dados.json'

# Chamar a função e obter os resultados
menor, menor_validos, maior, dias_acima_media,faturamento_total = processar_faturamento(caminho_arquivo)

# Exibir os resultados
print(f"Menor faturamento em um dia: R$ {menor:.2f}")
print(f"Menor faturamento em um dia valido: R$ {menor_validos:.2f}")
print(f"Maior faturamento em um dia: R$ {maior:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
print(f"Faturamento Mensal: {faturamento_total}")

######### PERGUNTA 04

percentuais = {}
for estado, faturamento in faturamentos_estados.items():
    percentual = (faturamento / faturamento_total) * 100
    percentuais[estado] = percentual

# Exibindo os resultados
for estado, percentual in percentuais.items():
    print(f"Percentual do estado: {estado}: {percentual:.2f}%")