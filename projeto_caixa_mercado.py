import requests

produtos = int(input('Digite [1] para iniciar e [2] para parar'))
total1 = 0
total2 = 0
prodcont = 0
while produtos == 1:
    produtos2 = int(input('Você tem produtos para passar ? [1]Sim [2]Não: '))
    prodcont += 1
    #PARA A REPETIÇÃO SE FOR "2" E DIMINUI 1 DA CONTAGEM DE PRODUTOS
    if produtos2 == 2:
        prodcont -= 1
        break
    #PERGUNTA O VALOR DA COMPRA E ADICIONA O VALOR NA VARIAVEL TOTAL1
    if produtos2 == 1:
        valor = int(input('Qual o valor da compra? '))
        total1 = valor
    #SE NAO PARA A REPETIÇÃO
    else:
        break
    #PERGUNTA SE TEM CUPOM DE DESCONTO
    if produtos2 == 1:
        cupom = int(input('Tem cupom de desconto? [1]Sim [2]Não: '))
    #SE SIM PARA PRODUTOS E CUPOM PERGUNTA O VALOR DO DESCONTO DO CUPOM
    if produtos2 == 1 and cupom == 1:
        desconto = int(input('Qual o valor do desconto do cupom ?(sera descontado em porcentagem): '))
    #CRIA A CONTA DE DESCONTO E ADICIONA O VALOR DA COMPRA COM DESCONTO A VARIAVEL TOTAL2
        desconto1 = valor*desconto/100
        total2 = valor - desconto1
    #SE NAO TIVER CUPOM REINICIA O LOOP PERGUNTANDO SE TEM PRODUTOS
    elif produtos2 == 1 and cupom == 2:
        produtos2
    else:
        break
print('O programa terminou!!!')
#MOSTRA QUANTOS PRODUTOS PASSARAM, E O TOTAL DA COMPRA
print(f'Você passou {prodcont} produtos, o valor da compra é: {total1+total2}')
