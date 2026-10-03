hp_noel = 100
dano_breu = 15
fator_continente = 1.0
modificador = 1.0
fim = 0
localidade = ''
presente = 0
presentestotais = 0
carvao = 0
carvoestotais = 0
custoglobal = 0

while (hp_noel > 0) and (localidade != 'FIM'):
    localidade = str(input())
    # print(f'A localidade é {localidade}')
    custolocal = 0
    custobase = 10

    if localidade != 'FIM':
        continente = str(input())

        if continente == 'Europa':
            fator_continente = 1.0
        elif continente == 'Oceania':
            fator_continente = 2.0
        elif continente == 'América':
            fator_continente = 3.0
        elif continente == 'África':
            fator_continente = 4.0
        elif continente == 'Ásia':
            fator_continente = 5.0
        else:
            fator_continente = 1.0

        pais = str(input())

        if pais == 'Brasil':
            modificador = 1.10
        elif pais == 'EUA':
            modificador = 1.15
        elif pais == 'China':
            modificador = 1.20
        elif pais == 'Canadá':
            modificador = 1.25
        elif pais == 'Rússia':
            modificador = 1.30
        else:
            modificador = 1.00

        nome = ''
        sobrecarga = 0

        while nome != 'FIM_LOCAL':
            nome = str(input())

            if nome != 'FIM_LOCAL':

                if custolocal <= 100:
                    custobase = 10
                elif custolocal > 100:
                    custobase = 15

                if 'Breu' in nome:
                    print('Alerta! Breu atacou a entrega!')
                    iniciativa = str(input())
                    hp_breu = 50
                    contador_noel = 0
                    contador_breu = 0

                    if 'Noel' in iniciativa:
                        contador_noel += 1
                    elif 'Breu' in iniciativa:
                        contador_breu +=1

                    while (hp_noel > 0) and (hp_breu > 0):
                        atacar = str(input()) # To achando que esse atacar nao ta fazendo nada ????

                        if contador_breu < contador_noel: 
                            hp_breu -= 20 
                            contador_breu +=1
                        elif contador_breu > contador_noel: 
                            hp_noel -= dano_breu
                            contador_noel += 1
                        elif contador_breu == contador_noel: 
                            if 'Breu' in iniciativa:
                                hp_breu -= 20
                                contador_breu += 1
                            elif 'Noel' in iniciativa:
                                hp_noel -= dano_breu
                                contador_noel +=1
                    else:
                        if hp_noel <= 0:
                            nome = 'FIM_LOCAL'
                            localidade = 'FIM'
                        elif hp_breu <= 0: # Noel ganhou, ler nova criança ou evento
                            print('Noel repeliu a emboscada e as entregas continuam!')
                        
                elif 'Breu' not in nome: # Entrega
                    nota = int(input())
                    custo = (custobase * fator_continente * modificador)
                    custolocal += custo
                    custoglobal += custo
                    print(f'o custo local é {custolocal}')
                    print(f'o custo base é {custobase}')

                    while (nota < 0) or (nota > 100):
                        print('Pontuação inválida, insira novamente.')
                        nota = int(input())

                    if nota >= 70:
                        print(f'{nome} foi uma boa criança este ano e receberá um presente!')
                        presente += 1
                        presentestotais += 1
                        # print(presente)
                        carvao = 0 # Dar um presente zera a sequência de carvão

                        if presente == 3: # Combo presente
                            print('A fé das crianças fortalece a magia! Noel recuperou 10 de HP.')
                            hp_noel += 10
                            presente = 0

                            if hp_noel > 100: # Ajustando a vida do noel
                                hp_noel = 100

                    elif nota < 70:
                        print(f'{nome} não se comportou bem e receberá carvão.')
                        carvao += 1
                        carvoestotais += 1
                        presente = 0 # Dar um carvão zera a sequência de presentes

                        if carvao == 3: # Combo carvão
                            dano_breu += 5
                            print(f'O medo e a descrença alimentam as sombras... O dano de Breu aumentou para {dano_breu}!')
                            carvao = 0

                    if (custolocal > 100) and (sobrecarga == 0): # Botei assim para garantir que só será lido uma vez na localidade
                        print('O trenó está sobrecarregado pela magia! Custos base aumentados.')
                        sobrecarga = 1

            elif nome == 'FIM_LOCAL':
                # print('finalizou')
                print(f'Localidade {localidade} finalizada. Custo logístico: {custolocal:.2f}')

else:
    if (localidade == 'FIM') and (hp_noel > 0):
        print(f'Noite concluída com sucesso! Presentes: {presentestotais} | Carvão: {carvoestotais}')
        print(f'Custo logístico total: {custoglobal:.2f}')
        print(f'HP final do Noel: {hp_noel}')
    elif hp_noel <= 0:
        print('O HP de Noel chegou a zero! O Breu venceu a batalha... O Natal das crianças foi arruinado.')