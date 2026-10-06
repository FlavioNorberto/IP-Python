cena = []
quadrante = []
sangue = 0
arma = 0
smiley = 'Nao'
matriz_evidencia = []

print('--- FASE 1: A VARREDURA ---')

n_linhas = int(input())

for i in range(n_linhas): # Não posso usar len(n_linhas) pois o inteiro não tem lenght
    item = input()
    # cena += item # OBS: ISSO AQUI NÃO FUNCIONA! O += com uma lista e uma string faz o Python adicionar cada caractere da string separadamente.
    cena.append(item.split(', ')) 

# Dados da submatriz
linha_inicio, linha_fim, coluna_inicio, coluna_fim = input().split()

linha_inicio = int(linha_inicio)
linha_fim = int(linha_fim)
coluna_inicio = int(coluna_inicio)
coluna_fim = int(coluna_fim)

for i in range(linha_inicio, linha_fim):
    linha = [] # Necessário criar uma lista aqui para armazenar os elementos da submatriz para depois appendar

    for j in range(coluna_inicio, coluna_fim):
        linha.append(cena[i][j])

    quadrante.append(linha)

print('Lisbon: Jane, focamos as buscas no quadrante delimitado.')

for i in range(len(quadrante)): # len(quadrante) recebe a quantidade de linhas
    for j in range(len(quadrante[i])): # len(quadrante[i]) recebe a quantidade de elementos naquela linha.
        valor = quadrante[i][j]

        if valor == 'Sangue':
            sangue += 1
        elif valor == 'Arma':
            arma += 1
        elif valor == 'Smiley':
            smiley = 'Sim' 

for linha in quadrante:
    print(linha)

print(f'Evidencias encontradas: Sangue ({sangue}), Arma ({arma}). Smiley ({smiley})')
print()

print('--- FASE 2: A MATRIZ DE EVIDÊNCIAS ---')

numero_linhas_matriz_evidencias, numero_colunas_matriz_evidencias = input().split()

numero_linhas_matriz_evidencias = int(numero_linhas_matriz_evidencias)
numero_colunas_matriz_evidencias = int(numero_colunas_matriz_evidencias)

# Construindo a matriz evidência
for i in range(numero_linhas_matriz_evidencias):
    valores = input().split()
    matriz_evidencia.append(valores)

limiar_evidencia = int(input())

for i in range(len(matriz_evidencia)):
    for j in range(len(matriz_evidencia[i])):
        valor = int(matriz_evidencia[i][j]) # Preciso converter para inteiro para fazer o condicional do if, se não valor será uma string e não vou conseguir fazer

        if valor >= limiar_evidencia:
            matriz_evidencia[i][j] = 1
        else:
            matriz_evidencia[i][j] = 0

print('Patrick Jane: Às vezes, a verdade está escondida bem diante dos nossos olhos.')

assinatura = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

linhas_assinatura = len(assinatura)
colunas_assinatura = len(assinatura[0])

encontrado = []

for i in range(numero_linhas_matriz_evidencias - linhas_assinatura + 1):
    for j in range(numero_colunas_matriz_evidencias - colunas_assinatura + 1):

        igual = True

        for a in range(linhas_assinatura):
            for b in range(colunas_assinatura):

                if matriz_evidencia[i + a][j + b] != assinatura[a][b]:
                    igual = False

        if igual:
            encontrado.append([i, j])

for linha in matriz_evidencia:
    print(*linha)

assinatura_encontrada = len(encontrado) > 0

if assinatura_encontrada:
    print('Patrick Jane: Eu conheço esse sorriso.')
    print('RED JOHN DEIXOU UMA ASSINATURA!')
    print(f'ASSINATURA ENCONTRADA EM [{encontrado[0][0]}][{encontrado[0][1]}]')
else:
    print('Patrick Jane: Nada aqui parece familiar.')

print()

caso_red = (smiley == 'Sim') or assinatura_encontrada

if caso_red:
    print('--- FASE 3: A MENSAGEM ---')
    alfabeto = "abcdefghijklmnopqrstuvwxyz "

    texto = input().split()
    numeros = []
    
    for i in texto: 
        numeros.append(int(i))

    caractere = []

    for i in numeros:

        if i % 2 == 0:
            caractere.append(alfabeto[(i // 2) % 27])
        else:
            caractere.append(alfabeto[(i * 3 + 1) % 27])

    mensagem = ''.join(caractere)
    
    print(f'Mensagem decodificada: "{mensagem}"')
    print('Jane: Ele acha que é mais esperto que eu. Nós vamos pegá-lo.')

else:
    print('--- FASE 3: O CÓDIGO ---')
    texto = input()
    invertido = texto[::-1]
    selecionada = invertido[::2]  

    resultado = ""

    for c in selecionada:  
        if c.islower():
            resultado += c.upper()
        elif c.isupper():
            resultado += c.lower()
        else:  # nao é letra
            resultado += c

    grau_obsessao = 0

    for c in resultado:
        if c == 'J' or c == 'j':
            grau_obsessao += 1
    print('Patrick Jane: Vamos ver o que ele quis dizer dessa vez.')
    print('MENSAGEM DECODIFICADA!')
    print(f"Patrick Jane: '{resultado}'...")
    print('Patrick Jane: Esse caso acabou de dar uma reviravolta interessante.')
    print(f'Grau de Obsessão: {grau_obsessao} aparição(ões) da letra J na mensagem.')
    print('--- CASO ENCERRADO (por enquanto...) ---')