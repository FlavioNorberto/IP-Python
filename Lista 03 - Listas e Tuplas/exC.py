reagentes_base = ("Metilamina", "Fenilacetona", "Hidróxido de Sódio", "Ácido Clorídrico", "Metilamina")
quantidades_ml = (500, 250, 150, 100, 300)
funcionando = True

print('Sistema HeisenbergOS v2.0 - Monitor do Reator Inicializado...')
print() # Quebra de linha

operador = str(input())
pressao_tanque = str(input())
status_mike = str(input())

# FASE 1
if not pressao_tanque.isnumeric():
    print('Yo Jesse! Você colocou tempero onde devia ter um número de pressão! O reator pifou!')
    funcionando = False
elif pressao_tanque.isnumeric():
     pressao_tanque = int(pressao_tanque)

if funcionando == True:
    # FASE 2
    if operador == 'Hank Schrader' or operador == 'Gomez':
        print('Alerta Vermelho: Agente do DEA detectado no laboratório!')

    if status_mike.isupper():
        print('Abaixe o tom de voz! Mike está escutando no microfone!')

    # FASE 3
    acao = str(input())
    while acao != 'FIM':

        if acao == 'contar':
            ingrediente_alvo = str(input())
            indice = reagentes_base.index(ingrediente_alvo)
            quantidades = 0

            for i in range(len(reagentes_base)):
                if reagentes_base[i] == ingrediente_alvo:
                    quantidades += 1

            if ingrediente_alvo not in reagentes_base:
                print(f'O Ingrediente {ingrediente_alvo} não foi encontrado, precisamos melhorar o nosso estoque!')
            else:
                print(f'O ingrediente {ingrediente_alvo} aparece {quantidades} vez(es) na receita base.')

        elif acao == 'posicao':
            ingrediente_alvo = str(input())
            posicao = reagentes_base.index(ingrediente_alvo)

            if ingrediente_alvo not in reagentes_base:
                print(f'Ingrediente {ingrediente_alvo} nao encontrado no registro fixo!')
            else:
                print(f'O ingrediente {ingrediente_alvo} foi encontrado primeiro na posicao {posicao} da tupla.')

        elif acao == 'varrer':
            ingrediente_alvo = str(input())
            soma = 0

            for i in range(len(reagentes_base)):
                if reagentes_base[i] == ingrediente_alvo:
                    quantidade = quantidades_ml[i]
                    print(f'Lote encontrado: {ingrediente_alvo} - {quantidade}ml')
                    soma += quantidade

            print(f'Volume total de {ingrediente_alvo} no reator: {soma}ml')


        elif acao == 'concatenar':
            novo_elemento = str(input())
            nova_quantidade = str(input())
            reagentes_base = reagentes_base + (novo_elemento, )
            quantidades_ml = quantidades_ml + (nova_quantidade, )
            print( f'Ingrediente adicionado à nova tupla! Tamanho atualizado: {len(reagentes_base)}')

        elif acao == 'desempacotar':
            r1 = reagentes_base[-3]
            m1 = quantidades_ml[-3]
            r2 = reagentes_base[-2]
            m2 = quantidades_ml[-2]
            r3 = reagentes_base[-1]
            m3 = quantidades_ml[-1]
            print(f'Últimos 3 reativos do registro: {r1} ({m1}ml), {r2} ({m2}ml) e {r3} ({m3}ml).')

        acao = str(input())

    if (pressao_tanque >= 50) or (status_mike.lower() == 'tranquilo'):
        print('Reação perfeita! Lote de 99.1% de pureza pronto para distribuição.')
    elif pressao_tanque < 15:
        print('Pressão crítica muito baixa! A mistura estragou, descarte o lote!')
    elif status_mike.lower() == 'alerta' and (len(reagentes_base) > 5):
        print('A receita ficou muito complexa para o tempo hábil! Limpe o reator antes que Mike chegue!')
    else:
        print('Ajustando exaustores... Mantenha o reator sob observação!')