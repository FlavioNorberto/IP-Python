kit_rick = ["colt_357", "distintivo", "radio_comunicador", "cantil", "curativo"]
kit_michonne = ["katana", "amolador", "binoculo", "faixa_curativo", "mapa"]
kit_daryl = ["arco e flecha","flechas","faca_de_caca", "corda", "carne_seca"]
kit_carol = ["facao", "bomba_de_fumaca", "sangue_zumbi", "fosforos", "biscoito"]

kit  = ["taco_beisebol","besta","kit_medico", "feijao_enlatado", "walkie_talkie", "garrafa_agua","biscoito"]

companheiro = input()
kit_companheiro = []

if companheiro == 'Rick':
    print('Um grande líder sempre ajuda sua equipe, Rick lhe dá uma lanterna para a noite')
    kit.append('lanterna')
    kit_companheiro = kit_rick
elif companheiro == 'Michonne':
    print('Michonne é uma ótima combatente, ela te dá uma arma para você não passar apertos.')
    kit.append('faca_afiada')
    kit_companheiro = kit_michonne
elif companheiro == 'Daryl':
    print('Daryl é um ótimo caçador. Ele te dá carne para comer na refeição')
    kit.append('carne')
    kit_companheiro = kit_daryl
elif companheiro == 'Carol':
    print('Carol sabe como se esconder dos zumbis. Ela te dá uma ajuda.')
    kit.append('roupa_de_camuflagem')
    kit_companheiro = kit_carol

# PRIMEIRO DIA

if companheiro == 'Rick': 
    kit.remove('taco_beisebol')
    kit_rick.append('taco_beisebol')

    print(f'Kit atual sobrevivente: {kit}')

elif companheiro == 'Michonne':
    kit.remove('kit_medico')

    print('Você usou o kit médico para socorrer Michonne!')
    print(f'Kit atual sobrevivente: {kit}')

elif companheiro == 'Daryl':
    kit[kit.index('besta')] = 'arco e flecha'
    kit_daryl[kit_daryl.index('arco e flecha')] = 'besta'

    print(f'Kit atual sobrevivente: {kit}')
    print(f'Kit atual Daryl: {kit_daryl}')

elif companheiro == 'Carol':
    kit_carol.remove('bomba_de_fumaca')
    kit_carol.remove('sangue_zumbi')
    kit_carol.remove('fosforos')

    # del kit[2:4] # Assim eu to removendo os itens 2 e 3 da lista. Mas como faço para irem para ela? Vou fazer como sei

    kit.remove('kit_medico') # Considerando que nos primeiros ifs o valor ta sendo armazenado no final, na ordem o intem de índice 2 é o kit médico e o de índice 3 é o feijão
    kit.remove('feijao_enlatado')

    kit_carol.append('kit_medico')
    kit_carol.append('feijao_enlatado')

# SEGUNDO DIA

if companheiro == 'Rick': 
    # Nesse caso, o kit tá assim kit  = ["besta","kit_medico", "feijao_enlatado", "walkie_talkie", "garrafa_agua","biscoito", "lanterna"]. Logo, o primeiro e segundo item é besta e kit médico
    kit.remove('feijao_enlatado')
    kit.remove('walkie_talkie')
    kit.remove('garrafa_agua')
    kit.remove('biscoito')
    kit.remove('lanterna')

    kit_rick.append('feijao_enlatado')
    kit_rick.append('walkie_talkie')
    kit_rick.append('garrafa_agua')
    kit_rick.append('biscoito')
    kit_rick.append('lanterna')

    print('Agora com as costas mais leves, podemos continuar com a nossa caminhada\n')

elif companheiro == 'Michonne': # Nesse caso, o kit tá assim: kit  = ["taco_beisebol","besta", "feijao_enlatado", "walkie_talkie", "garrafa_agua","biscoito", "faca_afiada"]. Então os dois primeiros itens são taco e besta
    kit.remove('feijao_enlatado')
    kit.remove('walkie_talkie')
    kit.remove('garrafa_agua')
    kit.remove('biscoito')
    kit.remove('faca_afiada')

    kit_michonne.append('feijao_enlatado')
    kit_michonne.append('walkie_talkie')
    kit_michonne.append('garrafa_agua')
    kit_michonne.append('biscoito')
    kit_michonne.append('faca_afiada')

    print('Agora com as costas mais leves, podemos continuar com a nossa caminhada\n')

elif companheiro == 'Daryl': # Nesse caso, o kit tá assim: kit  = ["taco_beisebol", "arco e flecha", "kit_medico", "feijao_enlatado", "walkie_talkie", "garrafa_agua","biscoito", "carne"]. Nesse caso, o taco e o kit médico são os dois primeiros.
    kit.remove('kit_medico')
    kit.remove('feijao_enlatado')
    kit.remove('walkie_talkie')
    kit.remove('garrafa_agua')
    kit.remove('biscoito')
    kit.remove('carne')

    kit_daryl.append('kit_medico')
    kit_daryl.append('feijao_enlatado')
    kit_daryl.append('walkie_talkie')
    kit_daryl.append('garrafa_agua')
    kit_daryl.append('biscoito')
    kit_daryl.append('carne')

    print('Agora com as costas mais leves, podemos continuar com a nossa caminhada\n')

elif companheiro == 'Carol': # Nesse caso, o kit tá assim: kit  = ["taco_beisebol","besta", "walkie_talkie", "garrafa_agua","biscoito", "roupa_de_camuflagem"]. Os primeiros são taco e besta
    kit.remove('walkie_talkie')
    kit.remove('garrafa_agua')
    kit.remove('biscoito')
    kit.remove('roupa_de_camuflagem')

    kit_carol.append('walkie_talkie')
    kit_carol.append('garrafa_agua')
    kit_carol.append('biscoito')
    kit_carol.append('roupa_de_camuflagem')

    print('Agora com as costas mais leves, podemos continuar com a nossa caminhada\n')

# TERCEIRO DIA

print('Finalmente chegamos em Alexandria!\n')
print(f'Ufa, podemos ficar aqui por um tempo,{companheiro}\n')
print(f'Kit do sobrevivente: {kit}')
print()
print(f'Kit do {companheiro}: {kit_companheiro}')