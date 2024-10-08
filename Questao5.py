def inverter(s):

    invertida = ""
    
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    
    return invertida

entrada = "Estágio em Análise e Desenvolvimento"
resultado = inverter(entrada)

print("String original:", entrada)
print("String invertida:", resultado)