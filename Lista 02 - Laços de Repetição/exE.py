# Antes do desfecho
ataquestotais = int(input())
desfecho = 0
derrota = 0

print('Quando percebi que contara oito mortes, senti o peso da minha própria lenda')

if ataquestotais > 0:
    ataques = 0
    while (ataques < ataquestotais) and (desfecho == 0): # O ciclo se repete até esgotar as tentativas ou até o Gato ganhar coragem para ir ao Desfecho.
        print('Preciso encontrar esse mapa a qualquer custo, nem que seja a última coisa que eu faça com esta vida!')
        companheiro = str(input())
        ataques += 1
        if companheiro == 'cao perrito':
            print('Olha só... de todas as criaturas do mundo, justo você tinha que decidir me seguir com esse rabo abanando?')
            numeros = int(input())
            n = 0
            divisivel = 1
            soma = 0
            while (n < numeros) and (divisivel == 1):
                valor = int(input())
                n += 1
                soma += valor
                if valor % 3 != 0:
                    divisivel = 0
            if soma % 3 == 0:
                print('Bom trabalho, meu garoto! Quem diria que um cãozinho tão pequeno seria o grande herói do dia?')
                desfecho = 1
        elif companheiro == 'kitty patamansa':
            print('Kitty... Olhar para você de novo só me faz lembrar que, entre todas as minhas nove vidas, o meu maior erro foi ter deixado você esperando.')
            item = str(input())
            if item == 'chapeu do gato' or item == 'bota do gato':
                print('Impressionante, Kitty... Sempre soube que você era rápida, mas admito que nada fica melhor nas mãos da melhor ladra de Tão Tão Distante do que um presente para mim.')
                desfecho = 1
        else:
            frase = str(input())
            if 'Desfecho' in frase:
                desfecho = 1
            while ('Desfecho' not in frase) and ('Morte' not in frase):
                frase = str(input())
                if 'Desfecho' in frase:
                    desfecho = 1


    if (ataques == ataquestotais) and (desfecho == 0):
        print('Pode levar minha espada e meu chapéu... Eu lutei até o fim, mas hoje a lenda finalmente descansa.')
        derrota = 1
    else:
        print('Parece que essa família de ursos e sua cachinhos acabam de provar do verdadeiro felino de botas!')
        frase_gato = str(input()).lower()
        if 'coragem' in frase_gato:
            print('A verdadeira vitória não está em vencer a morte, mas em encará-la de frente e escolher lutar por cada segundo desta vida!')
            derrota = 0
        else:
            print('Pode levar minha espada e meu chapéu... Eu lutei até o fim, mas hoje a lenda finalmente descansa.')
            derrota = 1

elif ataquestotais == 0:
    print('Até logo, velho amigo... É bom saber que finalmente posso respirar fundo e apenas viver o dia de hoje.')
    coragem = 0