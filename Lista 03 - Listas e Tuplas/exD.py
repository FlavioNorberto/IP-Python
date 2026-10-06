temperatura_lista = []
frequencia_pulso_lista = []
troca_gasosa_lista = []
homeostase_lista = []

critico = 0
avaliacao_final = ''

print('Espaço: a fronteira final. Estas são as viagens da nave estelar Enterprise…')
print('Sua missão de cinco anos: explorar novos mundos, procurar novas vidas e novas civilizações, audaciosamente indo aonde nenhum homem jamais esteve.')
print('Dr. McCoy: Eu sou um médico, não um matemático. Mas tenho que fazer o que precisa ser feito.')
print('=====')


# PRIMEIRA FASE - AMOSTRAS SAUDÁVEIS
tamanho_amostra = int(input())
while (tamanho_amostra < 5) or (tamanho_amostra > 12):
    print('Dr. McCoy: Esse número não é ideal, é possível trazer uma amostra de 5 a 12 indivíduos?')
    tamanho_amostra = int(input())
else:
    print(f'Dr. McCoy: Certo, {tamanho_amostra} indivíduos. É um número bom.')
    print('=====')

    for i in range(tamanho_amostra):
        amostras = input().split(' - ')

        temperatura_saudavel = float(amostras[0].replace(' °C', ''))
        frequencia_pulso_saudavel = float(amostras[1].replace(' bpm', ''))
        troca_gasosa_saudavel = float(amostras[2].replace(' irpm', ''))
        homeostase_saudavel = float(amostras[3].replace(' mmHg', ''))

        temperatura_lista.append(temperatura_saudavel)
        frequencia_pulso_lista.append(frequencia_pulso_saudavel)
        troca_gasosa_lista.append(troca_gasosa_saudavel)
        homeostase_lista.append(homeostase_saudavel)

# Colocando em ordem
temperatura_lista.sort()
frequencia_pulso_lista.sort()
troca_gasosa_lista.sort()
homeostase_lista.sort()

# Mediana temperatura
if len(temperatura_lista) % 2 == 0:
    meio_01_temperatura = temperatura_lista[len(temperatura_lista) // 2]
    meio_02_temperatura = temperatura_lista[((len(temperatura_lista) // 2) - 1)]
    mediana_temperatura = round((meio_01_temperatura + meio_02_temperatura) / 2 , 1)
else:
    mediana_temperatura = round(temperatura_lista[len(temperatura_lista) // 2] , 1)

# Mediana frequência de pulso
if len(frequencia_pulso_lista) % 2 == 0:
    meio_01_frequencia_pulso = frequencia_pulso_lista[len(frequencia_pulso_lista) // 2]
    meio_02_frequencia_pulso = frequencia_pulso_lista[((len(frequencia_pulso_lista) // 2) - 1)]
    mediana_frequencia_pulso = round((meio_01_frequencia_pulso + meio_02_frequencia_pulso) / 2 , 1)
else:
    mediana_frequencia_pulso = round(frequencia_pulso_lista[len(frequencia_pulso_lista) // 2] , 1)

# Mediana troca gasosa
if len(troca_gasosa_lista) % 2 == 0:
    meio_01_troca_gasosa = troca_gasosa_lista[len(troca_gasosa_lista) // 2]
    meio_02_troca_gasosa = troca_gasosa_lista[((len(troca_gasosa_lista) // 2) - 1)]
    mediana_troca_gasosa = round((meio_01_troca_gasosa + meio_02_troca_gasosa) / 2 , 1)
else:
    mediana_troca_gasosa = round(troca_gasosa_lista[len(troca_gasosa_lista) // 2] , 1)

# Mediana homeostase
if len(homeostase_lista) % 2 == 0:
    meio_01_homeostase = homeostase_lista[len(homeostase_lista) // 2]
    meio_02_homeostase = homeostase_lista[((len(homeostase_lista) // 2) - 1)]
    mediana_homeostase = round((meio_01_homeostase + meio_02_homeostase) / 2 , 1)
else:
    mediana_homeostase = round(homeostase_lista[len(homeostase_lista) // 2] , 1)

print('Relatório de dados da amostra:')
print(f'Temperatura: {temperatura_lista}')
print(f'Mediana: {mediana_temperatura}')
print(f'Frequência de pulso fluido: {frequencia_pulso_lista}')
print(f'Mediana: {mediana_frequencia_pulso}')
print(f'Frequência de troca gasosa: {troca_gasosa_lista}')
print(f'Mediana: {mediana_troca_gasosa}')
print(f'Pressão interna de homeostase: {homeostase_lista}')
print(f'Mediana: {mediana_homeostase}')
print('=====')

# SEGUNDA FASE - PACIENTE
print('Dr. McCoy: Agora irei medir os sinais do paciente.')
print('=====')

paciente = input().split(' - ')
critico = 0

temperatura_paciente = float(paciente[0].replace(' °C', ''))
frequencia_pulso_paciente = float(paciente[1].replace(' bpm', ''))
troca_gasosa_paciente = float(paciente[2].replace(' irpm', ''))
homeostase_paciente = float(paciente[3].replace(' mmHg', ''))

if (temperatura_paciente < temperatura_lista[0]) or (temperatura_paciente > temperatura_lista[-1]):
    critico += 1

if (frequencia_pulso_paciente < frequencia_pulso_lista[0]) or (frequencia_pulso_paciente > frequencia_pulso_lista[-1]):
    critico += 1

if (troca_gasosa_paciente < troca_gasosa_lista[0]) or (troca_gasosa_paciente > troca_gasosa_lista[-1]):
    critico += 1

if (homeostase_paciente < homeostase_lista[0]) or (homeostase_paciente > homeostase_lista[-1]):
    critico +=1

if critico >= 2:
    avaliacao_final = 'Alerta Crítico'
else:
    avaliacao_final = 'Estável'


print('Relatório final:')
print(f'Temperatura do paciente: {temperatura_paciente}')
print(f'Diferença para a mediana: {round(temperatura_paciente - mediana_temperatura , 1)}')
print(f'Frequência de pulso fluido do paciente: {frequencia_pulso_paciente}')
print(f'Diferença para a mediana: {round(frequencia_pulso_paciente - mediana_frequencia_pulso , 1)}')
print(f'Frequência de troca gasosa: {troca_gasosa_paciente}')
print(f'Diferença para a mediana: {round(troca_gasosa_paciente - mediana_troca_gasosa , 1)}')
print(f'Pressão interna de homeostase: {homeostase_paciente}')
print(f'Diferença para a mediana: {round(homeostase_paciente - mediana_homeostase , 1)}')
print(f'Quantidade de sinais críticos encontrados: {critico}')
print(f'Avaliação final: {avaliacao_final}')
print('=====')
print('Dr. McCoy: Certo, agora sei o que fazer.')