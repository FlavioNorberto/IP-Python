quantidade_linhas = int(input())
quantidade_colunas = int(input())

matriz = []
coluna = []

operando = True

# 1) Validação das dimensões
if (quantidade_linhas <= 0) or (quantidade_colunas <= 0):
    print('Dimensões do mapa inválidas!')
    operando = False

if operando == True:
    print('Avatar: A Lenda de Aang - Planejamento da Invasão!')
    print('Sokka: Mapeando os setores da Nação do Fogo...')

    for i in range(quantidade_linhas):
        linha = [] # Eu preciso criar uma nova linha depois que a anterior for preenchida, por isso esse linha = [] precisa ser dentro do for, se não, ele não cria uma nova linha e adiciona os próximos valores dentro da mesma linha

        for j in range(quantidade_colunas):
            elemento = int(input())

            # 2) Amplificação de Convergência — Diagonais
            if i == j: # Diagonal Principal - Se o índice da linha for igual ao índice da coluna, multiplique o valor da célula por 2.
                elemento *= 2

            if (quantidade_linhas == quantidade_colunas) and ((i + j) == (quantidade_linhas - 1)): # Diagonal Secundária - A diagonal secundária só será considerada quando a matriz for quadrada, ou seja, quando o número de linhas for igual ao número de colunas. Se o número de linhas for igual ao número de colunas e a soma dos índices da linha e da coluna for igual ao número de linhas menos 1, some 5 ao valor da célula.
                elemento += 5

            # 3) Filtro de Segurança
            if elemento < 15:
                elemento = 0

            if elemento % 2 != 0:
                elemento += 1

            linha.append(elemento)

        matriz.append(linha)

    # Imprimir a matriz
    for linha in matriz:
        print(*linha) # Serve para dar espaço entre os números e, dessa forma, coloca uma linha embaixo da outra
    
    # 4) Cálculo do relatório
    soma = 0

    # Soma Total de Resistência
    for linha in matriz:
        for elemento in linha:
            soma += elemento

    # Setor Mais Crítico
    maior_valor = matriz[0][0]
    linha_maior = 0
    coluna_maior = 0

    for i in range(quantidade_linhas):
        for j in range(quantidade_colunas):
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
                linha_maior = i
                coluna_maior = j

    # Comparação entre os valores dentro da matriz, se há mais números pares ou mais números ímpares
    quantidade_pares = 0
    quantidade_impares = 0

    for linha in matriz:
        for elemento in linha:
            if (elemento % 2 == 0):
                quantidade_pares += 1
            else:
                quantidade_impares += 1

    print('--- RELATÓRIO DO TÚNEL E AMEAÇAS ---')
    print(f'Soma Total de Resistência: {soma}') # A Soma Total de Resistência corresponde à soma de todos os valores da matriz após o processamento.
    print(f'Setor Mais Crítico: ({linha_maior}, {coluna_maior}) com valor {maior_valor}') # O Setor Mais Crítico é a posição (linha, coluna) que contém o maior valor da matriz processada.

    if soma < 100: # Invasão tranquila
        print('Sokka: O mapa revela poucas defesas inimigas!')
        print('Aang: Parece que o caminho está livre.')
        print('Katara: Conseguimos passar sem grandes problemas!')
        print('Estratégia aprovada! O Avatar está pronto para a batalha.')
    elif (soma >= 100) and (soma < 200):
        print('Sokka: Atenção! Detectamos resistência nas defesas da Nação do Fogo.')
        print('Toph: Sinto muitas tropas pelo solo, mas podemos avançar com cuidado.')
        print('Aang: Então vamos atentos. A Equipe Avatar está pronta!')
        print('Estratégia aprovada, mas a invasão será realizada com cautela.')
    elif soma >= 200:
        print('Sokka: Alerta! As defesas inimigas são muito fortes!')
        print('Toph: A linha de defesa deles é densa demais para atravessarmos.')
        print('Aang: Então precisamos recuar e repensar nosso plano.')
        print('Alerta vermelho: Nível de ameaça crítico! Invasão adiada.')

    aliado = str(input())
    limite_energia = int(input())

    # Aang
    if aliado == 'Aang':
        if (soma <= limite_energia): # Aang foi bem sucedido
            print(f'{aliado} usou sua especialidade com maestria e garantiu o sucesso na missão!')
        else:
            print(f'{aliado} encontrou barreiras intransponíveis e a missão precisou ser abortada...')

    # Katara
    if aliado == 'Katara':
        if (quantidade_pares > quantidade_impares): # Katara será bem sucedida
            print(f'{aliado} usou sua especialidade com maestria e garantiu o sucesso na missão!')
        else:
            print(f'{aliado} encontrou barreiras intransponíveis e a missão precisou ser abortada...')

    # Toph
    if aliado == 'Toph':
        if maior_valor <= 50:
            print(f'{aliado} usou sua especialidade com maestria e garantiu o sucesso na missão!')
        else:
            print(f'{aliado} encontrou barreiras intransponíveis e a missão precisou ser abortada...')

    # Sokka
    if aliado == 'Sokka':
        if quantidade_linhas == quantidade_colunas:
            print(f'{aliado} usou sua especialidade com maestria e garantiu o sucesso na missão!')
        else:
            print(f'{aliado} encontrou barreiras intransponíveis e a missão precisou ser abortada...')