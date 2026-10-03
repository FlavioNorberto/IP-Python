N = int(input())

vagas = ''

repeticoes = 0
ineditos = 0

for i in range(N):

    cargo = input()

    if cargo in vagas:

        repeticoes += 1

    else:
        if vagas != '':
            vagas = vagas + ' - '

        vagas = vagas + cargo
        ineditos += 1


print('Parabéns formandos! E agora iniciaremos sua carreira nas indústrias Honex.')

print(vagas)

print(f'Quantidade de cargos repetidos: {repeticoes}')

if ineditos > repeticoes:
    print('Pelo menos Barry tem opções!')
else:
    print('Mais do mesmo. Barry será apenas uma engrenagem na máquina de mel.')