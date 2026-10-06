lista_herois = []
lista_ameacas = []
criterio_prioritario = ""
pontuacao_extra = 0
pontuacao_total = 0
classificacao_herois = []
nivel_dificuldade = 0
categoria_ameaca = ""
qtd_herois_necessarios = 0
qtd_herois_disponiveis = 0
equipe_final = []

print('========================================')
print('GDA - HERO DISPATCH SYSTEM')
print('========================================')

# Cadastro dos heróis
entrada = str(input())

while entrada != 'FIM':

    dados = entrada.split(" - ")

    nome_heroi = dados[0]
    forca = int(dados[1])
    resistencia = int(dados[2])
    velocidade = int(dados[3])
    inteligencia = int(dados[4])
    experiencia = int(dados[5])

    lista_herois.append((nome_heroi, forca, resistencia, velocidade, inteligencia, experiencia))

    entrada = str(input())

print('[ROBOT] Sistema de despacho iniciado.')
print(f'[ROBOT] {len(lista_herois)} heróis disponíveis.')

# Leitura das ameaças
total_ameacas = int(input())

for indice in range(total_ameacas):
    print('========================================')
    print('NOVA AMEAÇA DETECTADA')
    print('========================================')

    entrada = str(input())

    dados = entrada.split(" - ")

    nome_ameaca = dados[0]
    nivel_dificuldade = int(dados[1])
    criterio_prioritario = dados[2]
    lista_ameacas.append((nome_ameaca, nivel_dificuldade, criterio_prioritario))

    print(f'AMEAÇA: {nome_ameaca}')
    print(f'NÍVEL DE DIFICULDADE: {nivel_dificuldade}')
    print(f'PRIORIDADE: {criterio_prioritario}')

    print('[ROBOT] Analisando heróis disponíveis...')
    print('[ROBOT] Calculando compatibilidade...')
    print('[ROBOT] Análise concluída.')

    # Cálculo da pontuação de cada herói
    classificacao_herois = []

    for heroi in lista_herois:

        nome_heroi = heroi[0]
        forca = heroi[1]
        resistencia = heroi[2]
        velocidade = heroi[3]
        inteligencia = heroi[4]
        experiencia = heroi[5]

        pontuacao_total = forca + resistencia + velocidade + inteligencia + experiencia

        if criterio_prioritario == 'Força':
            pontuacao_extra = forca
        elif criterio_prioritario == 'Resistência':
            pontuacao_extra = resistencia
        elif criterio_prioritario == 'Velocidade':
            pontuacao_extra = velocidade
        elif criterio_prioritario == 'Inteligência':
            pontuacao_extra = inteligencia
        elif criterio_prioritario == 'Experiência':
            pontuacao_extra = experiencia

        pontuacao_total = pontuacao_total + pontuacao_extra

        classificacao_herois.append((nome_heroi, pontuacao_total, pontuacao_extra))

    # Ordenação
    tamanho = len(classificacao_herois)

    for i in range(tamanho - 1):
        for j in range(tamanho - 1 - i):
            item_atual = classificacao_herois[j]
            item_seguinte = classificacao_herois[j + 1]
            deve_trocar = False

            if item_atual[1] < item_seguinte[1]:
                deve_trocar = True
            elif item_atual[1] == item_seguinte[1] and item_atual[2] < item_seguinte[2]:
                deve_trocar = True

            if deve_trocar:
                classificacao_herois[j] = item_seguinte
                classificacao_herois[j + 1] = item_atual

    print('========================================')
    print('RANKING DE HERÓIS')
    print('========================================')
    for posicao in range(len(classificacao_herois)):
        print(f'{posicao + 1}. {classificacao_herois[posicao][0]} - {classificacao_herois[posicao][1]} pontos')
    print('----------------------------------------')

    # Definindo quantos heróis serão despachados
    if nivel_dificuldade <= 30:
        categoria_ameaca = 'SIMPLES'
        qtd_herois_necessarios = 1
    elif nivel_dificuldade <= 70:
        categoria_ameaca = 'MODERADA'
        qtd_herois_necessarios = 2
    else:
        categoria_ameaca = 'CRÍTICA'
        qtd_herois_necessarios = 3

    print(f'[ROBOT] Ameaça {categoria_ameaca}.')
    print(f'[ROBOT] {qtd_herois_necessarios} herói(s) serão despachados.')

    # Verificando disponibilidade de heróis
    qtd_herois_disponiveis = len(lista_herois)

    if qtd_herois_disponiveis < qtd_herois_necessarios:
        print('[ROBOT] ALERTA!')
        print(f'[ROBOT] São necessários {qtd_herois_necessarios} heróis,')
        print(f'[ROBOT] mas apenas {qtd_herois_disponiveis} estão disponíveis.')
        print('[ROBOT] Despachando todos os heróis disponíveis.')
        qtd_herois_necessarios = qtd_herois_disponiveis
    else:
        print('[CECIL] Equipe selecionada para a missão.')

    equipe_final = classificacao_herois[:qtd_herois_necessarios]
    print('EQUIPE DESPACHADA:')
    for membro in range(len(equipe_final)):
        print('> ' + equipe_final[membro][0])
    print('========================================')