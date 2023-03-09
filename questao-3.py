import json

def main():
    data = ler_json('dados.json')

    valores = []

    for item in data:
        if(item['valor'] != 0):
            valores.append(item['valor'])

    print("Menor valor: ", menorValor(valores))
    print("Maior valor: ", maiorValor(valores))
    print("Dias no mes em que o valor de faturamento diario foi superior a media mensal: ", superiorMedia(valores))

def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)
    

def menorValor(valores):

    menor = valores[0]

    for i in range(1, len(valores)):
        if(valores[i] < menor):
            menor = valores[i]

    return menor

def maiorValor(valores):
    maior = valores[0]

    for i in range(1, len(valores)):
        if(valores[i] > maior):
            maior = valores[i]

    return maior

def superiorMedia(valores):
    soma = 0
    for item in valores:
        soma = soma + item
    
    media = soma / len(valores)

    dias = 0

    for i in range(len(valores)):
        if(valores[i] > media):
            dias = dias + 1

    return dias

main()