print('=== WABAC: SISTEMA DE EMERGÊNCIA ===')
print('Alvo: Ano 2026 | Peças Necessárias: 3')
print('Sherman, mantenha as mãos longe dos botões! Iniciando saltos...')

ano_origem = int(input()) # onde a viagem se inicia
ano_proibido = int(input()) # Ano em que já existe uma versão no passado.
energia = int(input())

parada = 0

ano_atual = ano_origem
rasgo_temporal = 0
pecas = 0

contagem = 0

# Possíveis saídas
paradoxo = False
apagao = False
colapso = False
abortar = False
missaocumprida = False

while parada == 0:
    acao = str(input())
    contagem += 1

    if acao == 'SALTAR':
        anos_salto = int(input())
        custo_energia = int(input())
        ano_atual += anos_salto
        energia -= custo_energia
        rasgo_temporal += 10

        if energia < 0: # Normalizando os limites
            energia = 0

        if rasgo_temporal > 100:
            rasgo_temporal = 100 # Normalizando

        if (ano_atual == ano_proibido) or ((ano_atual == ano_origem) and contagem > 1):
            parada = 1 # Paradoxo das duplicatas
            paradoxo = True
        elif energia <= 0:
            parada = 1 # Apagão temporal
            apagao = True
        elif rasgo_temporal >= 100:
            parada = 1 # Colapso dimensional
            colapso = True
        elif (pecas >= 3) and (ano_atual >= 2026):
            parada = 1 # Missão cumprida
            missaocumprida = True

        if parada == 0:
            print(f'WABAC saltou para o ano {ano_atual}!')
            print(f'Energia restante: {energia} | Rasgo Temporal: {rasgo_temporal}%')

    elif acao == 'CONSERTAR':
        dificuldade = int(input())
        esforco_sherman = int(input())

        if esforco_sherman >= dificuldade:
            pecas += 1
            energia -= 10

            if energia < 0: # Normalizando
                energia = 0

            if energia <= 0:
                parada = 1 # Apagão temporal
                apagao = True
            elif (pecas >= 3) and (ano_atual >= 2026):
                parada = 1 # Missão cumprida
                missaocumprida = True

            if parada == 0:
                print('Sherman: "Consegui, Mr. Peabody! Encontrei uma peça de calibragem!"')
                print(f'Peças coletadas: {pecas}/3 | Energia: {energia}')

        elif esforco_sherman < dificuldade:
            energia -= 15
            rasgo_temporal += 20

            if energia < 0:
                energia = 0 # Normalizando

            if rasgo_temporal > 100: # Normalizando
                rasgo_temporal = 100

            if energia <= 0:
                parada = 1 # Apagão temporal
                apagao = True
            elif rasgo_temporal >= 100:
                parada = 1 # Colapso dimensional
                colapso = True

            if parada == 0:
                print('Mr. Peabody: "Tenha mais cuidado, Sherman! Essa falha desestabilizou o tempo!"')
                print(f'Energia: {energia} | Rasgo Temporal: {rasgo_temporal}%')

    elif acao == 'AULA DE HISTÓRIA':
        energia += 25
        rasgo_temporal += 15

        if rasgo_temporal > 100:
            rasgo_temporal = 100 # Normalizando

        if rasgo_temporal >= 100:
            parada = 1 # Colapso dimensional
            colapso = True

        if parada == 0:
            print('Mr. Peabody: "Como disse Galileu Galilei, a matemática é a linguagem com a qual Deus escreveu o universo."')
            print(f'Energia recarregada para {energia}!')

    elif acao == 'ABORTAR':
        parada = 1 # Comando de abortar
        abortar = True


if paradoxo == True:
    print(f'ALERTA CRÍTICO: Peabody encontrou sua própria versão no ano {ano_atual}!')
    print('O continuum espaço-tempo ruiu em uma espiral paradoxal.')
elif apagao == True:
    print('A WABAC desligou completamente por falta de energia.')
    print('Peabody e Sherman estão vagando sem rumo pela linha do tempo...')
elif colapso == True:
    print('O rasgo temporal atingiu massa crítica!')
    print('O universo foi engolido por um buraco negro sobre a cidade de Nova York.')
elif abortar == True:
    print('Mr. Peabody acionou o protocolo de parada manual.')
    print('A viagem foi cancelada antes de sua conclusão.')
elif missaocumprida == True:
    print(f'A WABAC emergiu com sucesso no ano de {ano_atual}! Com as 3 peças coletadas, Mr. Peabody selou o rasgo temporal e salvou o presente!')