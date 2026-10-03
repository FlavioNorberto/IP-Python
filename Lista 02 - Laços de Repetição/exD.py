rodadas = int(input())
n_rodada = 0
recorde = int(input())
total = 0

print('Tigresa: Duvido você bater o recorde, Po!')
print('Po: Prepare-se para ver o Dragão Guerreiro em ação!')

while n_rodada < rodadas and total < recorde:
    bandejas = int(input())
    bandejaatual = 0
    totalrodada = 0
    while bandejaatual < bandejas and totalrodada < recorde:
        bandejaatual += 1
        bolinhos = int(input())
        totalrodada = totalrodada + bolinhos
        total = total + bolinhos
    n_rodada += 1

    if totalrodada > recorde:
        print()
        print('Tigresa: Mas como?!')
        print('Po: UHUL! CONHEÇA A FORÇA DO DRAGÂO GUERREIRO!!')
        print(f'Rodada {n_rodada}: Po comeu {totalrodada} bolinhos.')
    elif totalrodada >= 10:
        print()
        print('Po: Delícia! Mais uma rodada finalizada!')
        print(f'Rodada {n_rodada}: Po comeu {totalrodada} bolinhos.')
    elif totalrodada < 10:
        print()
        print('Po: Ainda tenho espaço para mais!')
        print(f'Rodada {n_rodada}: Po comeu {totalrodada} bolinhos.')

if totalrodada > recorde:
    print()
    print('Po: Ei! Eu ainda não terminei!')
    print('Tigresa: Acho que não vou mais subestimar sua fome.')
    print(f'Que loucura! Po venceu a aposta comendo um total de {totalrodada} bolinhos em uma só rodada!')
elif total > recorde:
    print()
    print('Po: Eu sabia que conseguiria! O recorde e meu!')
    print('Tigresa: Inacreditável... Você realmente venceu a aposta.')
    print(f'Po venceu a aposta! Ele comeu um total de {total} bolinhos e superou o recorde de {recorde}!')
elif total == recorde:
    print()
    print('Po: Empatamos! Cheguei exatamente no recorde!')
    print('Tigresa: Impressionante, mas empatar não basta para vencer a aposta. Venha lavar a louça!')
    print(f'Houve um empate! Po comeu exatamente {total} bolinhos e igualou o recorde de {recorde}.')
else:
    print()
    print('Tigresa: Eu avisei, Po! A louça do palácio te espera.')
    print('Po: Ah não... Minhas mãos vão ficar enrugadas...')
    print(f'Tigresa venceu a aposta! Po comeu apenas {total} bolinhos e não alcançou o recorde de {recorde}.')