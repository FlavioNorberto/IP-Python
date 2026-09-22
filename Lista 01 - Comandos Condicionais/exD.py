chovendo = str(input())
temperatura = int(input())
energia = int(input())

if chovendo == 'S':
    if energia > 3:
        print('Brincar de bolinha no laboratório')
    elif energia <= 3:
        print('Soneca na caminha do CIn')
elif chovendo == 'N':
    if temperatura > 30:
        if energia >= 4:
            print('Nadar no lago da UFPE')
        elif energia < 4:
            print('Descansar na sombra da árvore')
    elif temperatura > 14 and temperatura < 31:
        if energia > 2:
            print('Longo passeio no parque')
        elif energia <= 2:
            print('Passeio curto no quarteirão')
    elif energia < 15:
        print('Passeio com roupinha de frio')