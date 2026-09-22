cidade1 = str(input())
veredito1 = str(input())

cidade2 = str(input())
veredito2 = str(input())

contagem = 0
gostou = 0
naogostou = 0

print('Depois que a Série A e a Libertadores ficaram só no sonho do Santa, Byte pendura a chuteira de ídolo tricolor e parte pro interior: começa a Excursão Interiorana em busca do time da sua vida!')

# Seguindo a ordem dos inputs. Primeiro analisando a cidade1 e o veredito1
if 'catende' in cidade1.lower():
    print('Catende!!! Aqui já rodou a maior usina de açúcar e álcool da América Latina, Byte sente o orgulho no ar.')
    if veredito1.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito1.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1
elif 'palmares' in cidade1.lower():
    print('Palmares, a Terra dos Poetas! Berço de nomes como Ascenso Ferreira, aqui até o futebol merece um verso.')
    if veredito1.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito1.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1
elif 'carcará' in cidade1.lower():
    print('Carcará no peito! Essa é terra de Salgueiro, o primeiro clube do interior a ser campeão pernambucano, Byte sente o chamado do Sertão!')
    contagem += 1
    if veredito1.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito1.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1
elif 'patativa' in cidade1.lower():
    print('Show da Patativa! Caruaru e o Central esperam Byte de braços abertos, direto da maior feira a céu aberto do mundo!')
    contagem += 1
    if veredito1.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito1.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1
elif 'azulão' in cidade1.lower():
    print('Ar puro de serra! O Azulão de Bonito, sensação recente do Pernambucano, pode ser o novo lar de Byte!')
    contagem += 1
    if veredito1.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito1.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1
elif 'fruticultura' in cidade1.lower():
    print('Margens do Velho Chico! Petrolina, a maior cidade do interior, com direito a manga, uva e muita irrigação, chama Byte pro time!')
    contagem += 1
    if veredito1.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito1.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1
elif 'pássaro preto' in cidade1.lower():
    print('Pertinho de casa! O Pássaro Preto, orgulhosamente um dos times mais folclóricos do planeta, também está de olho em Byte!')
    contagem += 1
    if veredito1.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito1.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1

# Cidade 2
if 'catende' in cidade2.lower():
    print('Catende!!! Aqui já rodou a maior usina de açúcar e álcool da América Latina, Byte sente o orgulho no ar.')
    if veredito2.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito2.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1
elif 'palmares' in cidade2.lower():
    print('Palmares, a Terra dos Poetas! Berço de nomes como Ascenso Ferreira, aqui até o futebol merece um verso.')
    if veredito2.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito2.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1
elif 'carcará' in cidade2.lower():
    print('Carcará no peito! Essa é terra de Salgueiro, o primeiro clube do interior a ser campeão pernambucano, Byte sente o chamado do Sertão!')
    contagem += 1
    if veredito2.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito2.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1
elif 'patativa' in cidade2.lower():
    print('Show da Patativa! Caruaru e o Central esperam Byte de braços abertos, direto da maior feira a céu aberto do mundo!')
    contagem += 1
    if veredito2.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito2.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1
elif 'azulão' in cidade2.lower():
    print('Ar puro de serra! O Azulão de Bonito, sensação recente do Pernambucano, pode ser o novo lar de Byte!')
    contagem += 1
    if veredito2.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito2.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1
elif 'fruticultura' in cidade2.lower():
    print('Margens do Velho Chico! Petrolina, a maior cidade do interior, com direito a manga, uva e muita irrigação, chama Byte pro time!')
    contagem += 1
    if veredito2.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito2.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1
elif 'pássaro preto' in cidade2.lower():
    print('Pertinho de casa! O Pássaro Preto, orgulhosamente um dos times mais folclóricos do planeta, também está de olho em Byte!')
    contagem += 1
    if veredito2.lower() == 'gostou':
        print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
        gostou += 1
    elif veredito2.lower() == 'não gostou':
        print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
        naogostou += 1

# Checando se passou por Catende e Palmares
if ('palmares' in cidade1.lower() and 'catende' in cidade2.lower()) or ('catende' in cidade1.lower() and 'palmares' in cidade2.lower()):
    print('Catende e Palmares na excursão? Aí sim Byte tá garimpando ouro puro da Zona da Mata Sul! Pena que acabou por aqui.')

print()

print('RELATÓRIO DA EXCURSÃO SERTANEJA DO BYTE:')
print(f'- Visitas que contaram: {contagem}')
print(f'- Gostou: {gostou}')
print(f'- Não gostou: {naogostou}')

print()

print('E assim termina a Excursão Interiorana de Byte em Pernambuco. Anotar tudo isso na unha, sem laço nem lista, dá um trabalhão! Nas próximas férias, Byte espera que a molecada já saiba de laços, listas e funções pra dar conta do recado com estilo :)')