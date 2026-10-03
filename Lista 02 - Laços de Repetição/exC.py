paciencia_shrek = int(input())
visitante = ''
qtd_visitantes = 0

print('Shrek achava que morar em um pântano afastado seria suficiente para manter as pessoas longe. Ele estava muito enganado.')

while paciencia_shrek >= 0 and visitante != 'ninguém':
    visitante = str(input())
    if visitante != 'ninguém':
        gasto_paciencia = int(input())
        paciencia_shrek = paciencia_shrek - gasto_paciencia
        if paciencia_shrek >= 0:
            if visitante == 'Burro':
                qtd_visitantes += 1
                print('Burro?! Eu acabei de pedir um pouco de paz!')
                assunto = str(input())
                if assunto == 'sanduíche':
                    print('Ah, isso sim é um bom assunto!')
                    gasto_paciencia = gasto_paciencia / 2
                elif assunto == 'Fiona':
                    print('É o Burro! E, como sempre, ele só sabe falar da Fiona.')
                elif assunto == 'pântano':
                    print('Burro, isso é MEU pântano...')
            elif visitante == 'Gato de Botas':
                qtd_visitantes += 1
                print('O Gato de Botas chegou! Shrek já está de olho nas suas botas.')
            elif visitante == 'Pinóquio':
                qtd_visitantes += 1
                print('Pinóquio chegou! Shrek espera que ele não esteja mentindo.')
            elif visitante == 'Lobo Mau':
                qtd_visitantes += 1
                print('Lobo Mau?! Shrek abriu a porta, mas já está se arrependendo!')
            else:
                qtd_visitantes += 1
                print('Visitante desconhecido! Shrek não sabe quem você é, mas pode entrar por sua conta em risco.')
    elif visitante == 'ninguém':
        print('Ufa! Ninguém apareceu. Finalmente, um pouco de paz no pântano!')


if paciencia_shrek < 0:
    print('A paciência do Shrek acabou! Dê meia-volta antes que ele perca o controle!')

print(f'Ao todo, {qtd_visitantes} visitantes passaram pelo pântano. Shrek sobreviveu a mais um dia!')