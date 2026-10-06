informacoes = input()
ameacas = ()
banco_completo = []

while informacoes != 'FIM':
    dados = informacoes.split(',')

    nome = str(dados[0])
    faccao = str(dados[1])
    DanoBase = float(dados[2])
    Inteligência = int(dados[3])
    FatorCaos = float(dados[4])

    # Nivel de ameaça
    nivel_inicial = DanoBase + (Inteligência * FatorCaos)

    if faccao == 'Enclave':
        nivel_ameaca = nivel_inicial - (nivel_inicial * 0.15)
    else:
        nivel_ameaca = nivel_inicial

    ameaca = ()
    ameaca += (-nivel_ameaca, )
    ameaca += (nome, )
    ameaca += (faccao, )

    ameacas += (ameaca, )

    banco_completo.append(ameaca)

    informacoes = input()

nova_lista = banco_completo[:]
faccoes = []

for ameaca in ameacas:
    faccoes.append(ameaca[2])
    
for i in range(len(nova_lista)):
    nivel_ameaca = -nova_lista[i][0] 
    nome = nova_lista[i][1]
    faccao = nova_lista[i][2]
    frequencia_faccao = faccoes.count(faccao)
    nivel_ajustado = nivel_ameaca + (nivel_ameaca * 0.05 * (frequencia_faccao - 1))
    nova_lista[i] = (-nivel_ajustado, nome, faccao)

nova_lista.sort()

# Zonas prioritárias
zona_prioritaria = nova_lista[:3]
zona_acompanhamento = nova_lista[3:]

print(zona_prioritaria)


'''
# Testando

print(nome)
print(faccao)
print(DanoBase)
print(Inteligência)
print(FatorCaos)


print(banco_completo)
'''



