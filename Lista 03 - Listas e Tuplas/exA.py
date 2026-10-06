lista_dwight = []
lista_jim = []
lista_stanley = []
lista_phillips = []
lista_michael = []

vendedor = ''

while vendedor.lower() != 'fim':
    vendedor = str(input())

    if vendedor.lower() != 'fim':
        empresa = str(input())

        if vendedor == 'Dwight':
            lista_dwight.append(empresa)
        elif vendedor == 'Jim':
            lista_jim.append(empresa)
        elif vendedor == 'Stanley':
            lista_stanley.append(empresa)
        elif vendedor == 'Phillips':
            lista_phillips.append(empresa)
        elif vendedor == 'Michael':
            lista_michael.append(empresa)
        else:
            lista_michael.append(empresa)

# Dwight
if len(lista_dwight) == 0:
    print('Dwight fez zero vendas hoje. Mais sorte amanhã!')
else:
    print(f'Dwight : {lista_dwight}')

# Jim
if len(lista_jim) == 0:
    print('Jim passou o dia fazendo pegadinhas e não concluiu nenhuma venda!')
else:
    print(f'Jim : {lista_jim}')

# Stanley
if len(lista_stanley) == 0:
    print('Stanley acabou dormindo em serviço, amanhã ele estará mais descansado!')
else:
    print(f'Stanley : {lista_stanley}')

# Phillips
if len(lista_phillips) == 0:
    print('Phillips se distraiu e acabou não fazendo vendas hoje!')
else:
    print(f'Phillips : {lista_phillips}')

# Michael
if len(lista_michael) == 0:
    print('Michael não trabalhou como vendedor hoje, apenas foi um bom chefe.')
else:
    print('Michael realizou vendas hoje!')
    print(f'Michael : {lista_michael}')