G = int(input())
print('Nossa, que lindo cavalo! Mas deixe-me verificar apenas uma coisa...')

dupla = G // 2

if G <= 0:
    print('ENTRADA LIBERADA')
else:
        print('ARMADILHA')
        if G % 2 == 0:
            print(f'OS GUERREIROS FORMARAM {dupla} DUPLAS')
        else:
            print(f'OS GUERREIROS FORMARAM {dupla} DUPLAS E UM GUERREIRO FICOU SOZINHO')